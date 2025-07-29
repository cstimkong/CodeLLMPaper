# Element-Based Automated DNN Repair with Fine-Tuned Masked Language Model

**Authors**: Wang, Xu and Zhang, Mingming and Meng, Xiangxin and Zhang, Jian and Liu, Yang and Hu, Chunming

**Abstract**:

Deep Neural Networks (DNNs) are prevalent across a wide range of applications. Despite their success, the complexity and opaque nature of DNNs pose significant challenges in debugging and repairing DNN models, limiting their reliability and broader adoption. In this paper, we propose MLM4DNN, an element-based automated DNN repair method. Unlike previous techniques that focus on post-training adjustments or rely heavily on predefined bug patterns, MLM4DNN repairs DNNs by leveraging a fine-tuned Masked Language Model (MLM) to predict correct fixes for nine predefined key elements in DNNs. We construct a large-scale dataset by masking nine key elements from the correct DNN source code and then force the MLM to restore the correct elements to learn the deep semantics that ensure the normal functionalities of DNNs. Afterwards, a light-weight static analysis tool is designed to filter out low-quality patches to enhance the repair efficiency. We introduce a patch validation method specifically for DNN repair tasks, which consists of three evaluation metrics from different aspects to model the effectiveness of generated patches. We construct a benchmark, BenchmarkAPR4DNN, including 51 buggy DNN models and an evaluation tool that outputs the three metrics. We evaluate MLM4DNN against six baselines on BenchmarkAPR4DNN, and results show that MLM4DNN outperforms all state-of-the-art baselines, including two dynamic-based and four zero-shot learning-based methods. After applying the fine-tuned MLM design to several prevalent Large Language Models (LLMs), we consistently observe improved performance in DNN repair tasks compared to the original LLMs, which demonstrates the effectiveness of the method proposed in this paper.

**Link**: [Read Paper](https://doi.org/10.1145/3715716)

**Labels**: [code generation](../../labels/code_generation.md), [program repair](../../labels/program_repair.md)
