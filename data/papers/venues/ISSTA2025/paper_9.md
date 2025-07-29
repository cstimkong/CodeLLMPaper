# Robust Vulnerability Detection across Compilations: LLVM-IR vs. Assembly with Transformer Model

**Authors**: Shir, Rony and Surve, Priyanka and Elovici, Yuval and Shabtai, Asaf

**Abstract**:

Detecting vulnerabilities in binary files is a challenging task in cybersecurity, particularly when source code is unavailable and the compilation process and its parameters are unknown. Existing deep learning-based detection methods often rely on knowing a binary’s specific compilation settings, which may limit their ability to perform well on other types of binaries. In this research, we provide a thorough comparison of assembly representation and LLVM-IR to identify which representation is more robust and suitable when compilation parameters are unknown. The choice of representation significantly influences detection accuracy. Another contribution of this paper is the use of CodeBERT, a transformer-based model, as a classification tool for detecting vulnerabilities in scenarios where the compilation process is unknown. This study applies   transformer models to the task of multi-class vulnerability detection in the LLVM-IR domain, with a focus on binary-derived representations. While recent research has explored the use of transformers for vulnerability analysis in source code and raw binary instruction streams, systematic evaluation as a classifier at the LLVMIR level remains limited. Prior work has commonly relied on RNN-based methods, which are considered state-of-the-art for this task; however, these models struggle to capture long-range dependencies effectively. To address this limitation, we extend transformer-based classification to LLVM-IR produced from binaries and provide a comprehensive evaluation in this setting. Our results highlight the potential of this approach to strengthen system security across diverse binary configurations.

**Link**: [Read Paper](https://doi.org/10.1145/3728903)

**Labels**: [static analysis](../../labels/static_analysis.md), [bug detection](../../labels/bug_detection.md), [code model](../../labels/code_model.md), [code model robustness](../../labels/code_model_robustness.md)
