# CodeFuse

<p align="center">
  <img src="assets/LOGO.png" width="50%" />
</p>


<div align="center">

[**简体中文**](https://github.com/codefuse-ai/.github/blob/main/profile/README_CN.md)|[**HF Repo**](https://huggingface.co/codefuse-ai)|[**ModelScope Repo**](https://modelscope.cn/organization/codefuse-ai)

</div>

## About

This repository lists key projects and related demos about CodeFuse. 

## About CodeFuse

CodeFuse aims to develop Code Large Language Models (Code LLMs) to support and enhance full-lifecycle AI native sotware developing, covering crucial stages such as design requirements, coding, testing, building, deployment, operations, and insight analysis. Below is the overall framework of CodeFuse. 
<p align="center">
  <img src="https://github.com/codefuse-ai/.github/assets/82250814/9c8cd9f3-b1ca-43a1-9b0f-8f612b06753e" width="90%" />
</p>
<br/>

## List of CodeFuse Projects

We listed projects according to the lifecycle above. 
| Stage               | Project Repository|  Description | Reference Models | 
|:------------------------:|:-----------------:|:-------:|:-------:|
| Project Copilot     |    NA             |     NA  |   NA    | 
| Code Copilot        |[MFTCoder](https://github.com/codefuse-ai/MFTCoder) | Instruction-Tuning Framework  |[CodeFuse-34B](https://huggingface.co/codefuse-ai/CodeFuse-CodeLlama-34B-4bits)   |
|                     |[FastTransformer4CodeFuse](https://github.com/codefuse-ai/FasterTransformer4CodeFuse) | FT based Inference Engine | MA |
|                     |[CodeFuse-Eval](https://github.com/codefuse-ai/codefuse-evaluation)|Evaluation kits for CodeFuse |   NA   |
| Test&Build Copilot  |[TestAgent](https://github.com/codefuse-ai/Test-Agent) | TestGPT demo frontend  |   NA   |
| Ops Copilot         |[DevOps-Eval](https://github.com/codefuse-ai/codefuse-devops-eval)|Benchmark for DevOps|   NA   | 
|                     |[DevOps-Model](https://github.com/codefuse-ai/CodeFuse-DevOps-Model) |index for DevOps  models|   NA   | 
| Data Copilot        |    NA              |     NA   |   NA   | 
| Auxilary Modules    |[ChatBot](https://github.com/codefuse-ai/codefuse-chatbot) |General chatbot frontend for CodeFuse |   NA   | 
|                     |This Repo |General Introduction & index of CodeFuse Repos|   NA   |


## Demos

 - Video demos: Chinese version at below, English version under preparation. 
   https://user-images.githubusercontent.com/103973989/267514150-21012a5d-652d-4aea-bcea-582e67855ad7.mp4

 - Online Demo: You can try our CodeFuse-CodeLlama-34B model on ModelScope: [CodeFuse-CodeLlama34B-MFT-Demo](https://modelscope.cn/studios/codefuse-ai/CodeFuse-CodeLlama34B-MFT-Demo/summary)

![Online Demo Snapshot](assets/modelscope_demo2.png)

- You can also try to install the [CodeFuse-Chatbot](https://github.com/codefuse-ai/codefuse-chatbot) to test our models locally. 

## How to get

- [**Huggingface Repo**](https://huggingface.co/codefuse-ai).
- [**ModelScope Repo**](https://modelscope.cn/organization/codefuse-ai).
- Train or finetuning on your own models, you can try our [**MFTCoder**](https://github.com/codefuse-ai/MFTCoder), which enables efficient fine-tuning for multi-task, multi-model, and multi-training-framework scenarios.

## Articles or References

For more details about our techniques, please refere to our tech-reports/papers below. 
- MFTCoder:

If you use our codes or models, or feel our project useful for your research works, please cite our paper as below.
```
@article{codefuse2023,
  title={},
  author={},
  journal={arXiv preprint arXiv},
  year={2023}
}

