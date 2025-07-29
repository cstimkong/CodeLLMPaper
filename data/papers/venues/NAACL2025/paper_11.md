# On the Impacts of Contexts on Repository-Level Code Generation

**Authors**: Hai, Nam Le  and      Nguyen, Dung Manh  and      Bui, Nghi D. Q.

**Abstract**:

CodeLLMs are widely used for code generation, yet their ability to handle repository-level dependencies remains underexplored. We introduce RepoExec, a benchmark for evaluating repository-level code generation, focusing on executability, functional correctness, and dependency utilization. Our study evaluates 18 models, revealing that retaining full dependency context yields the best performance, while smaller context sizes can be misleading. Pretrained LLMs excel in correctness but often reimplement dependencies, while instruction-tuned models better utilize dependencies but sometimes introduce unnecessary complexity. We propose an instruction-tuning dataset that improves dependency handling and introduce a new metric, Dependency Invocation Rate (DIR), to measure context utilization. Experiments show that instruction-tuned models improve DIR by over 10{\%}, and multi-round debugging further enhances both correctness and dependency use. RepoExec provides a comprehensive framework to advance CodeLLMs for real-world applications. The dataset and source code are available at \url{https://github.com/FSoft-AI4Code/RepoExec}.

**Link**: [Read Paper](https://aclanthology.org/2025.findings-naacl.82/)

**Labels**: [code generation](../../labels/code_generation.md), [program synthesis](../../labels/program_synthesis.md), [agent design](../../labels/agent_design.md), [prompt strategy](../../labels/prompt_strategy.md), [retrieval-augmented generation](../../labels/retrieval-augmented_generation.md)
