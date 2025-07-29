# Bridging Operator Semantic Inconsistencies: A Source-Level Cross-Framework Model Conversion Approach

**Authors**: Li, Xingpei and Lei, Yan and Jia, Zhouyang and Zhang, Yuanliang and Liu, Haoran and Chen, Liqian and Dong, Wei and Li, Shanshan

**Abstract**:

As deep learning (DL) frameworks become widely used, converting models between frameworks is crucial for ecosystem flexibility. However, interestingly, existing model converters commonly focus on syntactic operator API mapping—transpiling operator names and parameters—which results in API compatibility issues (i.e., incompatible parameters, missing operators). These issues arise from semantic inconsistencies due to differences in operator implementation, causing conversion failure or performance degradation. In this paper, we present the first comprehensive study on operator semantic inconsistencies through API mapping analysis and framework source code inspection, revealing that 47\% of sampled operators exhibit inconsistencies across DL frameworks, with source code limited to individual layers and no inter-layer interactions. This suggests that layer-wise source code alignment is feasible. Based on this, we propose ModelX, a source-level cross-framework conversion approach that extends operator API mapping by addressing semantic inconsistencies beyond the API level. Experiments on PyTorch-to-Paddle conversion show that ModelX successfully converts 624 out of 686 sampled operators and outperforms two state-of-the-art converters and three popular large language models. Moreover, ModelX achieves minimal metric gaps (avg. all under 3.4\%) across 52 models from vision, text, and audio tasks, indicating strong robustness.

**Link**: [Read Paper](https://doi.org/10.1145/3729361)

**Labels**: [code generation](../../labels/code_generation.md), [program transformation](../../labels/program_transformation.md), [empirical study](../../labels/empirical_study.md)
