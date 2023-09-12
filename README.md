# CodeFuse

<p align="left">
  <img src="assets/LOGO.png" width="100%" />
</p>


<div align="center">

[**简体中文**](https://github.com/codefuse-ai/.github/blob/main/profile/README_CN.md)|[**HF Repo**](https://huggingface.co/codefuse-ai)|[**ModelScope Repo**](https://modelscope.cn/organization/codefuse-ai)

</div>

## About

Hello World! This is CodeFuse! 


**The mission of CodeFuse is to develop Code Large Language Models (Code LLMs) specifically designed to support the entire software development lifecycle, covering crucial stages such as design, requirements, coding, testing, deployment, operations, and maintenance.** We are passionate about creating innovative solutions that empower developers throughout the software development process.

In this release, we are open sourcing 
1. **[The MFT (Multi-Task Fine-Tuning) framework, known as MFTCoder](https://github.com/codefuse-ai/MFTCoder);**
2. **Two datasets for enhancing the coding capabilities of LLMs, that is, [Code Exercise](https://huggingface.co/datasets/codefuse-ai/CodeExercise-Python-27k) and [Evol-Instruction](https://huggingface.co/datasets/codefuse-ai/Evol-instruction-66k);**
3. **[A faster and more reliable deployment framework based on FasterTransformer](https://github.com/codefuse-ai/FasterTransformer4CodeFuse).**

The resulting model ensemble, which includes [CodeFuse-13B](https://huggingface.co/codefuse-ai/CodeFuse-13B) ([ModelScope Repo](https://modelscope.cn/models/codefuse-ai/CodeFuse-13B/files))and [CodeFuse-CodeLlama-34B](https://huggingface.co/codefuse-ai/CodeFuse-CodeLlama-34B)([ModelScope Repo](https://modelscope.cn/models/codefuse-ai/CodeFuse-CodeLlama-34B/files)), supports various code-related tasks such as code completion, text-to-code conversion, and unit test generation. In particular, [CodeFuse-CodeLlama-34B](https://huggingface.co/codefuse-ai/CodeFuse-CodeLlama-34B), built upon CodeLlama as the base model and fine-tuned using the proposed MFT framework, achieves an impressive score of **74.4% (greedy decoding)** in the HumanEval Python pass@1 evaluation, **even surpassing the performance of GPT-4 (67%)**. We have plans to incorporate additional base LLMs into the ensemble in the near future.

We believe that our solution can significantly enhance the performance of pretrained LLMs across multiple related tasks simultaneously. We are committed to further exploring this direction and providing more open-source contributions. We also encourage engineers and researchers within this community to join us in co-constructing CodeFuse.


## Demo Video

<video src="https://github.com/codefuse-ai/codefuse/blob/master/assets/snake_game_codefuse.mp4" width="320" height="240" controls>
</video>


## Online Demo

You can try our CodeFuse-CodeLlama-34B model on ModelScope: [CodeFuse-CodeLlama34B-MFT-Demo](https://modelscope.cn/studios/codefuse-ai/CodeFuse-CodeLlama34B-MFT-Demo/summary)

