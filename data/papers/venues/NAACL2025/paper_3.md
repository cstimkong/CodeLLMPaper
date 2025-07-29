# {C}odex{G}raph: Bridging Large Language Models and Code Repositories via Code Graph Databases

**Authors**: Liu, Xiangyan  and      Lan, Bo  and      Hu, Zhiyuan  and      Liu, Yang  and      Zhang, Zhicheng  and      Wang, Fei  and      Shieh, Michael Qizhe  and      Zhou, Wenmeng

**Abstract**:

Large Language Models (LLMs) excel in stand-alone code tasks like HumanEval and MBPP, but struggle with handling entire code repositories. This challenge has prompted research on enhancing LLM-codebase interaction at a repository scale. Current solutions rely on similarity-based retrieval or manual tools and APIs, each with notable drawbacks. Similarity-based retrieval often has low recall in complex tasks, while manual tools and APIs are typically task-specific and require expert knowledge, reducing their generalizability across diverse code tasks and real-world applications. To mitigate these limitations, we introduce CodexGraph, a system that integrates LLM agents with graph database interfaces extracted from code repositories. By leveraging the structural properties of graph databases and the flexibility of the graph query language, CodexGraph enables the LLM agent to construct and execute queries, allowing for precise, code structure-aware context retrieval and code navigation. We assess CodexGraph using three benchmarks: CrossCodeEval, SWE-bench, and EvoCodeBench. Additionally, we develop five real-world coding applications. With a unified graph database schema, CodexGraph demonstrates competitive performance and potential in both academic and real-world environments, showcasing its versatility and efficacy in software engineering. Our code and demo will be released soon.

**Link**: [Read Paper](https://aclanthology.org/2025.naacl-long.7/)

**Labels**: [agent design](../../labels/agent_design.md), [prompt strategy](../../labels/prompt_strategy.md), [retrieval-augmented generation](../../labels/retrieval-augmented_generation.md)
