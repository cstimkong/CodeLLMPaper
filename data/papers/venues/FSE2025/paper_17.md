# An Adaptive Language-Agnostic Pruning Method for Greener Language Models for Code

**Authors**: Saad, Mootez and L\'{o}pez, Jos\'{e} Antonio Hern\'{a}ndez and Chen, Boqi and Varr\'{o}, D\'{a}niel and Sharma, Tushar

**Abstract**:

Language models of code have demonstrated remarkable performance across various software engineering and source code analysis tasks. However, their demanding computational resource requirements and consequential environmental footprint remain as significant challenges.               This work introduces ALPINE, an adaptive programming language-agnostic pruning technique designed to substantially reduce the computational overhead of these models.                The proposed method offers a pluggable layer that can be integrated with all Transformer-based models.                With ALPINE, input sequences undergo adaptive compression throughout the pipeline, reaching a size that is up to x3 less their initial size, resulting in significantly reduced computational load.               Our experiments on two software engineering tasks, defect prediction and code clone detection across three language models CodeBERT, GraphCodeBERT and UniXCoder show that ALPINE achieves up to a 50\% reduction in FLOPs, a 58.1\% decrease in memory footprint, and a 28.1\% improvement in throughput on average. This led to a reduction in CO2 emissions by up to 44.85\%. Importantly, it achieves a reduction in computation resources while maintaining up to 98.1\% of the original predictive performance.                These findings highlight the potential of ALPINE in making language models of code more resource-efficient and accessible while preserving their performance,               contributing to the overall sustainability of their adoption in software development.               Also, it sheds light on redundant and noisy information in source code analysis corpora, as shown by the substantial sequence compression achieved by ALPINE.

**Link**: [Read Paper](https://doi.org/10.1145/3715773)

**Labels**: [code model](../../labels/code_model.md), [code model training](../../labels/code_model_training.md)
