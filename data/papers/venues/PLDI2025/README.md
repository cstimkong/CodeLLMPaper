# PLDI2025

Number of papers: 4

## [DR.FIX: Automatically Fixing Data Races at Industry Scale](paper_1.md)
- **Authors**: Farnaz Behrang, Zhizhou Zhang, Georgian-Vlad Saioc, Peng Liu, Milind Chabbi
- **Abstract**: Data races are a prevalent class of concurrency bugs in shared-memory parallel programs, posing significant challenges to software reliability and reproducibility. While there is an extensive body of research on detecting data races and a wealth of practical detection tools across various programming languages, considerably less effort has been directed toward automatically fixing data races at an industrial scale. In large codebases, data races are continuously introduced and exhibit myriad pat...
- **Link**: [Read Paper](https://arxiv.org/abs/2504.15637)
- **Labels**: [code generation](../../labels/code_generation.md), [program repair](../../labels/program_repair.md)


## [Program Skeletons for Automated Program Translation](paper_3.md)
- **Authors**: Bo Wang, Tianyu Li, Ruishi Li, Umang Mathur, Prateek Saxena
- **Abstract**: Translating software between programming languages is a challenging task, for which automated techniques have been elusive and hard to scale up to larger programs. A key difficulty in cross-language translation is that one has to re-express the intended behavior of the source program into idiomatic constructs of a different target language. This task needs abstracting away from the source language-specific details, while keeping the overall functionality the same. In this work, we propose a nove...
- **Link**: [Read Paper](https://dl.acm.org/doi/10.1145/3729287)
- **Labels**: [code generation](../../labels/code_generation.md), [program transformation](../../labels/program_transformation.md)


## [Reductive Analysis with Compiler-Guided Large Language Models for Input-Centric Code Optimizations](paper_4.md)
- **Authors**: Xiangwei Wang, Xinning Hui, Chunhua Liao, Xipeng Shen
- **Abstract**: Input-centric program optimization aims to optimize code by considering the relations between program inputs and program behaviors. Despite its promise, a long-standing barrier for its adoption is the difficulty of automatically identifying critical features of complex inputs. This paper introduces a novel technique, reductive analysis through compiler-guided Large Language Models (LLMs), to solve the problem through a synergy between compilers and LLMs. It uses a reductive approach to overcome ...
- **Link**: [Read Paper](https://dl.acm.org/doi/10.1145/3729282)
- **Labels**: [static analysis](../../labels/static_analysis.md), [program optimization](../../labels/program_optimization.md)


## [Scalable, Validated Code Translation of Entire Projects using Large Language Models](paper_2.md)
- **Authors**: Hanliang Zhang, Cristina David, Meng Wang, Brandon Paulsen, Daniel Kroening
- **Abstract**: Large language models (LLMs) show promise in code translation due to their ability to generate idiomatic code. However, a significant limitation when using LLMs for code translation is scalability: existing works have shown a drop in translation success rates for code exceeding around 100 lines. We overcome this limitation by developing a modular approach to translation, where we partition the code into small code fragments which can be translated independently and semantically validated (that i...
- **Link**: [Read Paper](https://dl.acm.org/doi/10.1145/3729315)
- **Labels**: [code generation](../../labels/code_generation.md), [program transformation](../../labels/program_transformation.md)
