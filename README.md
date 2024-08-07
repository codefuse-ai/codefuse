# Index of CodeFuse Repositories

<p align="center">
  <img src="assets/LOGO.png" width="50%" />
</p>


<div align="center">

[**简体中文**](./README_CN.md)|[**HuggingFace**](https://huggingface.co/codefuse-ai)|[**ModelScope**](https://modelscope.cn/organization/codefuse-ai)

</div>

## About This Repository

This repository lists key projects and related demos about CodeFuse. 

## About CodeFuse

CodeFuse aims to develop Code Large Language Models (Code LLMs) to support and enhance full-lifecycle AI native sotware developing, covering crucial stages such as design requirements, coding, testing, building, deployment, operations, and insight analysis. Below is the overall framework of CodeFuse. 
<p align="center">
  <img src="https://github.com/codefuse-ai/.github/assets/82250814/9c8cd9f3-b1ca-43a1-9b0f-8f612b06753e" width="90%" />
</p>
<br/>


## Release Update
** 2024.07 **  [D2LLM](https://github.com/codefuse-ai/D2LLM) :  Release D2Coder-v1 Embedding model for code search, [RepoFuse](https://github.com/codefuse-ai) :  Repository-Level Code Completion with Language Models with Fused Dual Context

** 2024.06 **  [Codefuse-ai pages](https://codefuse-ai.github.io), [D2LLM](https://github.com/codefuse-ai/D2LLM) releases feature about Decomposed and Distilled Large Language Models for Semantic Search, [MFTCoder](https://github.com/codefuse-ai/MFTCoder) releases V0.4.2. More detail see [Release & Next Release](https://github.com/codefuse-ai/codefuse/issues/16)

** 2024.05 **  ModelCache releases v0.2.1 with supporting multimodal, see [CodeFuse-ModelCache](https://github.com/codefuse-ai/CodeFuse-ModelCache). DevOps-Model support function call, see [CodeFuse-DevOps-Model](https://github.com/codefuse-ai/CodeFuse-DevOps-Model). More detail see [Release & Next Release](https://github.com/codefuse-ai/codefuse/issues/14)

** 2024.04 ** CodeFuse-muAgent: a multi-agent framework, more detail see [Release & Next Release](https://github.com/codefuse-ai/codefuse/issues/12)

## List of CodeFuse Repositories

We listed repositories according to the lifecycle above. 
| LifeCycle Stage               | Project Repository|  Repo-Description | Road Map |
|:------------------------:|:-----------------:|:-------:|:------------------:|
| Requirement & Design     |[MFT-VLM](https://github.com/codefuse-ai/CodeFuse-MFT-VLM)            | Instruction-fine-tuning for Vision-language tasks  |       |
| Coding        |[MFTCoder](https://github.com/codefuse-ai/MFTCoder) | Instruction-Tuning Framework  |      |
|                     |[FastTransformer4CodeFuse](https://github.com/codefuse-ai/FasterTransformer4CodeFuse) | FT based Inference Engine |       |
|                     |[CodeFuse-Eval](https://github.com/codefuse-ai/codefuse-evaluation)|Evaluation kits for CodeFuse |         |
| Test & Build   |[TestAgent](https://github.com/codefuse-ai/Test-Agent) | TestGPT demo frontend  |        |
| DevOps         |[DevOps-Eval](https://github.com/codefuse-ai/codefuse-devops-eval)|Benchmark for DevOps|         |      |
|                     |[DevOps-Model](https://github.com/codefuse-ai/CodeFuse-DevOps-Model) |index for DevOps  models|         |
| Data Insight       |    NA              |     NA   |       |
| Base              |[ChatBot](https://github.com/codefuse-ai/codefuse-chatbot) |General chatbot frontend for CodeFuse |       |
|                     |[muAgent](https://github.com/codefuse-ai/CodeFuse-muAgent) | multi-agent framework |       |
|                     |[ModelCache](https://github.com/codefuse-ai/CodeFuse-ModelCache) |Semantic Cache for LLM Serving  |       |
|                     |[CodeFuse-Query](https://github.com/codefuse-ai/CodeFuse-Query)|Query-Based Code Analysis Engine |       |
| Others                     |[CoCA](https://github.com/codefuse-ai/Collinear-Constrained-Attention)|Colinear Attention |       |
|                     |[Awesine-Code-LLM](https://github.com/codefuse-ai/Awesome-Code-LLM)|Code-LLM Survey|       |
|                     |This Repo |General Introduction & index of CodeFuse Repos|       |

## List of CodeFuse Released Models

| ModelName               | Short Description | Modele Linls | 
|:------------------------:|:-----------------:|:-----------------:|
| CodeFuse-13B     | Training from scratch by CodeFuse | [HF](https://huggingface.co/codefuse-ai/CodeFuse-13B) ; [MS](https://modelscope.cn/models/codefuse-ai/CodeFuse-13B/summary)  | 
| CodeFuse-CodeLLaMA-34B    |    Finetuning on CodeLLaMA-34B  | [HF](https://huggingface.co/codefuse-ai/CodeFuse-CodeLlama-34B) ; [MS](https://modelscope.cn/models/codefuse-ai/CodeFuse-CodeLlama-34B/summary)  | 
| ** CodeFuse-CodeLLaMA-34B-4bits |  4bits quantized 34B model |[HF](CodeFuse-CodeLlama-34B-4bits) ; [MS](https://modelscope.cn/models/codefuse-ai/CodeFuse-CodeLlama-34B-4bits/summary)  | 
| CodeFuse-StarCoder-15B    | Finetuning on StarCoder-15B | [HF](https://huggingface.co/codefuse-ai/CodeFuse-StarCoder-15B) ; [MS](https://modelscope.cn/models/codefuse-ai/CodeFuse-StarCoder-15B/summary)  | 
| CodeFuse-Qwen-14B    | Finetuning on Qwen-14B           | [HF](https://huggingface.co/codefuse-ai/CodeFuse-QWen-14B) ; [MS](https://modelscope.cn/models/codefuse-ai/CodeFuse-QWen-14B/summary)  | 
| CodeFuse-CodeGeeX2-6B    | Finetuning on CodeGeeX2-6B           | [HF](https://huggingface.co/codefuse-ai/CodeFuse-CodeGeeX2-6B) ; [MS](https://modelscope.cn/models/codefuse-ai/CodeFuse-CodeGeeX2-6B/summary)  | 
| CodeFuse-DevOps-14B-Chat  | Finetuning on DevOps-14B           | [HF](https://huggingface.co/codefuse-ai/CodeFuse-DevOps-Model-14B-Chat) ; [MS](https://modelscope.cn/models/codefuse-ai/CodeFuse-DevOps-Model-14B-Chat/summary)  | 
| CodeFuse-DevOps-14B-Base    | Continue trianing on Qwen-14B           | [HF](https://huggingface.co/codefuse-ai/CodeFuse-DevOps-Model-14B-Base) ; [MS](https://modelscope.cn/models/codefuse-ai/CodeFuse-DevOps-Model-14B-Base/summary)  | 
| CodeFuse-TestGPT-7B    |   FineTuning on CodeLLaMA-7B   | [HF](https://huggingface.co/codefuse-ai/CodeFuse-TestGPT-7B) ; [MS](https://modelscope.cn/models/codefuse-ai/TestGPT-7B/summary)  | 
| CodeFuse-DeepSeek-33B | FineTuning on DeepSeek-Coder-33b | [HF](https://huggingface.co/codefuse-ai/CodeFuse-DeepSeek-33B) ; [MS](https://modelscope.cn/models/codefuse-ai/CodeFuse-DeepSeek-33B/summary) |
| ** CodeFuse-DeepSeek-33B-4bits | 4-bit quantized 33B model | [HF](https://huggingface.co/codefuse-ai/CodeFuse-DeepSeek-33B-4bits) ; [MS](https://modelscope.cn/models/codefuse-ai/CodeFuse-DeepSeek-33B-4bits/summary) |
| CodeFuse-Mixtral-8x7B | FineTuning on Mixtral-8x7B (MoE) | [HF](https://huggingface.co/codefuse-ai/CodeFuse-Mixtral-8x7B) ; [MS](https://modelscope.cn/models/codefuse-ai/CodeFuse-Mixtral-8x7B/summary) |
| CodeFuse-VLM-14B | SoTA vision-language model | [HF](https://huggingface.co/codefuse-ai/CodeFuse-VLM-14B) ; [MS]([https://modelscope.cn/models/codefuse-ai/CodeFuse-Mixtral-8x7B/summary](https://modelscope.cn/models/ss41979310/CodeFuse-VLM-14B/summary)) |

** -- recommended models;

## Demos

 - Video demos: Chinese version at below, English version under preparation.

   https://user-images.githubusercontent.com/103973989/267514150-21012a5d-652d-4aea-bcea-582e67855ad7.mp4

 - Online Demo: You can try our CodeFuse-CodeLlama-34B model on ModelScope: [CodeFuse-CodeLlama34B-MFT-Demo](https://modelscope.cn/studios/codefuse-ai/CodeFuse-CodeLlama34B-MFT-Demo/summary)

![Online Demo Snapshot](assets/modelscope_demo2.png)

- You can also try to install the [CodeFuse-Chatbot](https://github.com/codefuse-ai/codefuse-chatbot) to test our models locally. 

## How to get

- [**HuggingFace**](https://huggingface.co/codefuse-ai).
- [**ModelScope**](https://modelscope.cn/organization/codefuse-ai).
- [**WiseModel**](https://wisemodel.cn/organization/codefuse-ai).
- Train or finetuning on your own models, you can try our [**MFTCoder**](https://github.com/codefuse-ai/MFTCoder), which enables efficient fine-tuning for multi-task, multi-model, and multi-training-framework scenarios.

## Citation

For more technique details about CodeFuse, please refer to our paper [MFTCoder](https://arxiv.org/abs/2311.02303).

If you find our work useful or helpful for your R&D work, please feel free to cite our paper as follows.
```
@article{mftcoder2023,
      title={MFTCoder: Boosting Code LLMs with Multitask Fine-Tuning}, 
      author={Bingchang Liu and Chaoyu Chen and Cong Liao and Zi Gong and Huan Wang and Zhichao Lei and Ming Liang and Dajun Chen and Min Shen and Hailian Zhou and Hang Yu and Jianguo Li},
      year={2023},
      journal={arXiv preprint arXiv},
      archivePrefix={arXiv},
      eprint={2311.02303}
}
```

