# DecLLM: LLM-Augmented Recompilable Decompilation for Enabling Programmatic Use of Decompiled Code

**Authors**: Wong, Wai Kin and Wu, Daoyuan and Wang, Huaijin and Li, Zongjie and Liu, Zhibo and Wang, Shuai and Tang, Qiyi and Nie, Sen and Wu, Shi

**Abstract**:

Decompilers are widely used in reverse engineering (RE) to convert compiled executables into human-readable pseudocode and support various security analysis tasks. Existing decompilers, such as IDA Pro and Ghidra, focus on enhancing the readability of decompiled code rather than its recompilability, which limits further programmatic use, such as for CodeQL-based vulnerability analysis that requires compilable versions of the decompiled code. Recent LLM-based approaches for enhancing decompilation results, while useful for human RE analysts, unfortunately also follow the same path.    In this paper, we explore, for the first time, how off-the-shelf large language models (LLMs) can be used to enable recompilable decompilation—automatically correcting decompiler outputs into compilable versions. We first show that this is non-trivial through a pilot study examining existing rule-based and LLM-based approaches. Based on the lessons learned, we design DecLLM, an iterative LLM-based repair loop that utilizes both static recompilation and dynamic runtime feedback as oracles to iteratively fix decompiler outputs. We test DecLLM on popular C benchmarks and real-world binaries using two mainstream LLMs, GPT-3.5 and GPT-4, and show that off-the-shelf LLMs can achieve an upper bound of around 70\% recompilation success rate, i.e., 70 out of 100 originally non-recompilable decompiler outputs are now recompilable. We also demonstrate the practical applicability of the recompilable code for CodeQL-based vulnerability analysis, which is impossible to perform directly on binaries. For the remaining 30\% of hard cases, we further delve into their errors to gain insights for future improvements in decompilation-oriented LLM design.

**Link**: [Read Paper](https://doi.org/10.1145/3728958)

**Labels**: [code generation](../../labels/code_generation.md), [program decompilation](../../labels/program_decompilation.md)
