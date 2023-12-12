import os
import argparse
import tensorrt_llm
import torch
import platform
import json

import numpy as np
from tensorrt_llm.runtime import (
    ModelConfig, SamplingConfig, GenerationSession
)
from tensorrt_llm.runtime.generation import Mapping
from tensorrt_llm.quantization import QuantMode
from typing import List, Union, Optional
from pathlib import Path
from transformers import (AutoTokenizer,PreTrainedTokenizer)

now_dir = os.path.dirname(os.path.abspath(__file__))

EOS_TOKEN = 2
PAD_TOKEN = 0

from typing import List, Tuple

def to_word_list_format(words_list: List[List[str]], tokenizer):

    flat_ids = []
    offsets = []
    for words in words_list:
        item_flat_ids = []
        item_offsets = []

        for word in words:
            ids = tokenizer.encode(word,add_special_tokens=False)[1:]

            if len(ids) == 0:
                continue

            item_flat_ids += ids
            item_offsets.append(len(ids))

        flat_ids.append(np.array(item_flat_ids))
        offsets.append(np.cumsum(np.array(item_offsets)))

    pad_to = max(1, max(len(ids) for ids in flat_ids))

    for i, (ids, offs) in enumerate(zip(flat_ids, offsets)):
        flat_ids[i] = np.pad(ids, (0, pad_to - len(ids)), constant_values=0)
        offsets[i] = np.pad(offs, (0, pad_to - len(offs)), constant_values=-1)

    result = np.array([flat_ids, offsets], dtype="int32").transpose((1, 0, 2))
    return torch.from_numpy(np.ascontiguousarray(result))


def make_context(
    tokenizer: PreTrainedTokenizer,
    query: str,
    history: List[Tuple[str, str]] = None,
    system: str = "",
    max_input_length: int = 2048,
    chat_format: str = "MFT",
):
    if history is None:
        history = []

    if chat_format == "MFT":

        def _tokenize_str(role, content):
            role_dict = {"user": "human", "agent": "bot", "assistant": "bot", 
                    "<bot>": "bot", "<human>": "human", 
                    "<system>": "system","system": "system",
                    "humnan": "human", "bot":"bot"}
            eo_dict = {"bot": tokenizer.eos_token, "human": "", "system": ""}    
            if not content.endswith('\n'):
                content = content + '\n'
            return f"<s>{role_dict[role]}\n{content}{eo_dict[role_dict[role]]}"

        system_text = _tokenize_str("system", system)
        raw_text = ""
        context_tokens = []

        for turn_query, turn_response in reversed(history):
            query_text = _tokenize_str("user", turn_query)

            response_text = _tokenize_str(
                "assistant", turn_response
            )
            prev_chat = query_text+response_text

            raw_text = prev_chat + raw_text


            
        raw_text = system_text + raw_text

        query_content = _tokenize_str('user', query)
        raw_text = raw_text+query_content+'<s>bot'
        
        
    # truncate to max_input_length, truncate from the front
    return raw_text, tokenizer.encode(raw_text, add_special_tokens=False)[-max_input_length:]

def get_engine_name(model, dtype, tp_size, pp_size, rank):
    if pp_size == 1:
        return '{}_{}_tp{}_rank{}.engine'.format(model, dtype, tp_size, rank)
    return '{}_{}_tp{}_pp{}_rank{}.engine'.format(model, dtype, tp_size,
                                                  pp_size, rank)
def _clear_screen():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")

def read_config(config_path: Path):
    with open(config_path, 'r') as f:
        config = json.load(f)
    use_gpt_attention_plugin = config['plugin_config']['gpt_attention_plugin']
    remove_input_padding = config['plugin_config']['remove_input_padding']
    dtype = config['builder_config']['precision']
    tp_size = config['builder_config']['tensor_parallel']
    pp_size = config['builder_config']['pipeline_parallel']
    world_size = tp_size * pp_size

        
    num_heads = config['builder_config']['num_heads'] // tp_size
    hidden_size = config['builder_config']['hidden_size'] // tp_size
    vocab_size = config['builder_config']['vocab_size']
    num_layers = config['builder_config']['num_layers']
    num_kv_heads = config['builder_config'].get('num_kv_heads', num_heads)
    paged_kv_cache = config['plugin_config']['paged_kv_cache']
    tokens_per_block = config['plugin_config']['tokens_per_block']
    quant_mode = QuantMode(config['builder_config']['quant_mode'])
    if config['builder_config'].get('multi_query_mode', False):
        tensorrt_llm.logger.warning(
            "`multi_query_mode` config is deprecated. Please rebuild the engine."
        )
        num_kv_heads = 1
    use_custom_all_reduce = config['plugin_config'].get('use_custom_all_reduce',
                                                        False)

    model_config = ModelConfig(num_heads=num_heads,
                               num_kv_heads=num_kv_heads,
                               hidden_size=hidden_size,
                               vocab_size=vocab_size,
                               num_layers=num_layers,
                               gpt_attention_plugin=use_gpt_attention_plugin,
                               paged_kv_cache=paged_kv_cache,
                               tokens_per_block=tokens_per_block,
                               remove_input_padding=remove_input_padding,
                               dtype=dtype,
                               quant_mode=quant_mode,
                               use_custom_all_reduce=use_custom_all_reduce)

    return model_config, tp_size, pp_size, dtype



class LammaForCausalLMGenerationSession(GenerationSession):
    def __init__(
        self,
        model_config: ModelConfig,
        engine_buffer,
        mapping: Mapping,
        debug_mode=False,
        debug_tensors_to_save=None,
        cuda_graph_mode=False,
        stream: torch.cuda.Stream = None,
    ):
        super().__init__(
            model_config,
            engine_buffer,
            mapping,
            debug_mode,
            debug_tensors_to_save=debug_tensors_to_save,
            cuda_graph_mode=cuda_graph_mode,
            stream=stream
        )
        self.stop_words_list=to_word_list_format([['<s>human','<s>bot']], tokenizer).cuda()

    def prepare_for_chat(
        self,
        tokenizer,
        input_text: Union[str, List[str]],
        system_text: str = "",
        history: list = None,
        max_input_length: Union[int, None] = None,
    ):

        if history is None:
            history = []
        pad_id = tokenizer.pad_token_id
        # prepare for batch inference
        if not isinstance(input_text, list):
            batch_text = [input_text]
        else:
            batch_text = input_text
        if len(history) > 0 and len(history[0]) and len(history[0][0]) > 0 \
                and not isinstance(history[0][0], list):
            history_list = [history]
        elif len(history) == 0:
            history_list = [[]]
        else:
            history_list = history
        input_ids = []
        input_lengths = []

        for line, history in zip(batch_text, history_list):
            # use make_content to generate prompt
            _, input_id_list = make_context(
                tokenizer=tokenizer,
                query=line,
                history=history,
                system=system_text,
                max_input_length=max_input_length,
            )
            
            # print("input_id_list len", len(input_id_list))
            input_id = torch.from_numpy(
                np.array(input_id_list, dtype=np.int32)
            ).type(torch.int32).unsqueeze(0)
            input_ids.append(input_id)
            input_lengths.append(input_id.shape[-1])
        max_length = max(input_lengths)
        # do padding, should move outside the profiling to prevent the overhead
        for i in range(len(input_ids)):
            pad_size = max_length - input_lengths[i]

            pad = torch.ones([1, pad_size]).type(torch.int32) * pad_id
            input_ids[i] = torch.cat(
                [torch.IntTensor(input_ids[i]), pad], axis=-1)
        input_ids = torch.cat(input_ids, axis=0).cuda()
        input_lengths = torch.IntTensor(input_lengths).type(torch.int32).cuda()
        return input_ids, input_lengths
    
    def generate(
        self,
        input_ids: torch.Tensor,
        input_lengths: torch.Tensor,
        sampling_config: SamplingConfig,
        max_new_tokens: int,
        runtime_rank: int = 0,
        stop_works_list: Optional[torch.Tensor] = None
    ):
        max_input_length = torch.max(input_lengths).item()

        # setup batch_size, max_input_length, max_output_len
        self.setup(
            batch_size=input_lengths.size(0),
            max_context_length=max_input_length,
            max_new_tokens=max_new_tokens
        )
        output_ids = self.decode(
            input_ids,
            input_lengths,
            sampling_config,
            stop_words_list=self.stop_words_list
        )
        with torch.no_grad():
            torch.cuda.synchronize()
            if runtime_rank == 0:
                outputs = output_ids[:, 0, :]
                return outputs

    def chat_stream(
        self,
        tokenizer,
        sampling_config: SamplingConfig,
        input_text: Union[str, List[str]],
        max_input_length: Union[int, None],
        max_new_tokens: Union[int, None],
        system_text: str = "",
        history: list = None,
        runtime_rank: int = 0,
    ):
        input_ids, input_lengths = self.prepare_for_chat(
            tokenizer=tokenizer,
            input_text=input_text,
            system_text=system_text,
            history=history,
            max_input_length=max_input_length,
        )
        max_input_length = torch.max(input_lengths).item()

        self.setup(
            batch_size=input_lengths.size(0),
            max_context_length=max_input_length,
            max_new_tokens=max_new_tokens
        )
        with torch.no_grad():
            chunk_lengths = max_input_length
            for output_ids in self.decode(
                input_ids, input_lengths, sampling_config, streaming=True, stop_words_list = self.stop_words_list
            ):
                torch.cuda.synchronize()
                
                if runtime_rank == 0:
                    output_texts = []
                    for i in range(output_ids.size(0)):
                        temp_ids = output_ids[i, 0, max_input_length:]
                        temp_text = tokenizer.decode(temp_ids, skip_special_tokens=True)
                        # check code is error
                        if b"\xef\xbf\xbd" in temp_text.encode():
                            continue
                        chunk_lengths += 1
                        output_texts.append(temp_text)
                    if len(output_texts) > 0:
                        yield output_texts
def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('--max_new_tokens', type=int, default=512)
    parser.add_argument('--max_input_length', type=int, default=512)
    parser.add_argument('--log_level', type=str, default='error')
    parser.add_argument(
        '--engine_dir',
        type=str,
        default="",
    )
    parser.add_argument(
        '--tokenizer_dir',
        type=str,
        default="",
        help="Directory containing the tokenizer.model."
    )
    return parser.parse_args()


if __name__ == "__main__":
    # get model info
    args = parse_arguments()

    engine_dir = Path(args.engine_dir)
    config_path = engine_dir / 'config.json'
    model_config, tp_size, pp_size, dtype = read_config(config_path)

    world_size = tp_size * pp_size

    runtime_rank = tensorrt_llm.mpi_rank()
    runtime_mapping = tensorrt_llm.Mapping(world_size,
                                           runtime_rank,
                                           tp_size=tp_size,
                                           pp_size=pp_size)
    torch.cuda.set_device(runtime_rank % runtime_mapping.gpus_per_node)
    tokenizer = AutoTokenizer.from_pretrained(args.tokenizer_dir, legacy=False, use_fast=False)
    tokenizer.pad_token_id=PAD_TOKEN
    tokenizer.end_token_id=EOS_TOKEN
    
    sampling_config = SamplingConfig(end_id=EOS_TOKEN,
                                     pad_id=PAD_TOKEN,
                                     num_beams=1,
                                     )
    engine_name = get_engine_name('llama', dtype, tp_size, pp_size,
                                  runtime_rank)
    serialize_path = engine_dir / engine_name
    with open(serialize_path, 'rb') as f:
        engine_buffer = f.read()

    decoder = LammaForCausalLMGenerationSession(
        model_config,
        engine_buffer,
        runtime_mapping,
    )
    history = []
    response = ''
    print("Welcome :)")
    while True:
        input_text = input("User: ")
        if input_text in ["exit", "quit", "exit()", "quit()"]:
            break
        if input_text == 'clear':
            history = []
            continue
        
            # print("Output: ", end='')

        response = ""
        for new_text in decoder.chat_stream(
            tokenizer=tokenizer,
            sampling_config=sampling_config,
            input_text=input_text,
            history=history,
            max_new_tokens=args.max_new_tokens,
            max_input_length=args.max_input_length
        ):
            
            _clear_screen()
            print(f"\nUser: {input_text}")
            print(f"\nCodeFuse-ChatBot: {new_text[0]}")
        response += new_text[0]
        print("")
        
        history.append((input_text, response))
        # print(history)