# CodeFuse中文索引

<p align="center">
  <img src="assets/LOGO.png" width="50%" />
</p>


<div align="center">

[ **English** ](./README.md)|[ **HF Repo** ](https://huggingface.co/codefuse-ai)|[ **魔搭社区** ](https://modelscope.cn/organization/codefuse-ai)

</div>

## 关于本仓库

本仓库索引了CodeFuse项目的关键仓库、模型和演示例子. 

## 关于CodeFuse
CodeFuse的使命是开发专门设计用于支持整个软件开发生命周期的大型代码语言模型（Code LLMs），涵盖设计、需求、编码、测试、部署、运维等关键阶段。
我们致力于打造创新的解决方案，让软件开发者们在研发的过程中如丝般顺滑。下面是CodeFuse的整个框架。
<p align="center">
  <img src="https://github.com/codefuse-ai/.github/assets/82250814/9c8cd9f3-b1ca-43a1-9b0f-8f612b06753e" width="90%" />
</p>
<br/>

## CodeFuse仓库列表

我们按照上图软件生命周期的划分对仓库进行了组织. 
| 生命周期阶段               | 仓库名 | 仓库简介 | 
|:------------------------:|:-----------------:|:-------:|
| 项目Copilot     |    NA             |     NA  | 
| 数据Copilot        |[MFTCoder](https://github.com/codefuse-ai/MFTCoder) | CodeFuse独有的指令微调框架 |
|                     |[FastTransformer4CodeFuse](https://github.com/codefuse-ai/FasterTransformer4CodeFuse) | 推理引擎| 
|                     |[CodeFuse-Eval](https://github.com/codefuse-ai/codefuse-evaluation)|代码评估框架|   
| 测试和构建Copilot  |[TestAgent](https://github.com/codefuse-ai/Test-Agent) | TestGPT示例前端  |  
| 运维Copilot         |[DevOps-Eval](https://github.com/codefuse-ai/codefuse-devops-eval)|DevOps评测集和框架 |   
|                     |[DevOps-Model](https://github.com/codefuse-ai/CodeFuse-DevOps-Model) |DevOps模型列表介绍 |   
| 数据Copilot        |    NA              |     NA   | 
| 辅助模块   |[ChatBot](https://github.com/codefuse-ai/codefuse-chatbot) |通用chatbot前端 | 
|                     |你正在看的仓库 | CodeFuse通用介绍和索引 | 

## CodeFuse已发布模型索引

| ModelName               | Short Description | Modele Linls | 
|:------------------------:|:-----------------:|:-----------------:|
| CodeFuse-13B     | CodeFuse从0训练模型 | [HF](https://huggingface.co/codefuse-ai/CodeFuse-13B) ; [MS](https://modelscope.cn/models/codefuse-ai/CodeFuse-13B/summary)  | 
| CodeFuse-CodeLLaMA-34B    | 基于CodeLLaMA-34B微调的模型  | [HF](https://huggingface.co/codefuse-ai/CodeFuse-CodeLlama-34B) ; [MS](https://modelscope.cn/models/codefuse-ai/CodeFuse-CodeLlama-34B/summary)  | 
| ** CodeFuse-CodeLLaMA-34B-4bits |  34B模型的4bits量化版 |[HF](CodeFuse-CodeLlama-34B-4bits) ; [MS](https://modelscope.cn/models/codefuse-ai/CodeFuse-CodeLlama-34B-4bits/summary)  | 
| CodeFuse-StarCoder-15B    | 基于StarCoder-15B微调的模型 | [HF](https://huggingface.co/codefuse-ai/CodeFuse-StarCoder-15B) ; [MS](https://modelscope.cn/models/codefuse-ai/CodeFuse-StarCoder-15B/summary)  | 
| CodeFuse-Qwen-14B    | 基于Qwen-14B微调的模型    | [HF](https://huggingface.co/codefuse-ai/CodeFuse-QWen-14B) ; [MS](https://modelscope.cn/models/codefuse-ai/CodeFuse-QWen-14B/summary)  | 
| CodeFuse-TestGPT-7B    | 基于CodeLLaMA-7B微调的用于测试的模型 | [HF](https://huggingface.co/codefuse-ai/CodeFuse-TestGPT-7B) ; [MS](https://modelscope.cn/models/codefuse-ai/TestGPT-7B/summary)  | 


## 演示

 - 视频Demo: 下面是中文版本, 英文版准备中
   https://user-images.githubusercontent.com/103973989/267514150-21012a5d-652d-4aea-bcea-582e67855ad7.mp4

 - 在线版本: 你可以在魔搭社区尝试我们的34B模型: [CodeFuse-CodeLlama34B-MFT-Demo](https://modelscope.cn/studios/codefuse-ai/CodeFuse-CodeLlama34B-MFT-Demo/summary)

![Online Demo Snapshot](assets/modelscope_demo2.png)

- 离线版本：你也可以安装[CodeFuse-Chatbot](https://github.com/codefuse-ai/codefuse-chatbot)在本地尝试我们的模型.

## 如何获得

- HF模型社区[**Huggingface Repo**](https://huggingface.co/codefuse-ai).
- 魔搭社区[**ModelScope Repo**](https://modelscope.cn/organization/codefuse-ai).
- 对于自有或者自己感兴趣的模型，可以使用我们的[**MFTCoder**](https://github.com/codefuse-ai/MFTCoder)框架微调训练，它是一个支持多模型、多任务、多训练平台的微调框架.

## 参考文献

如需了解更多技术细节，可以参考我们的技术报告/论文. 
- MFTCoder:

如果你觉得我们的代码或者模型有用，或则给你的工作提供了一些有价值的参考，请引用我们的如下论文
```
@article{codefuse2023,
  title={},
  author={},
  journal={arXiv preprint arXiv},
  year={2023}
}
