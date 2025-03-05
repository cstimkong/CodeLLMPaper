# SGCode: A Flexible Prompt-Optimizing System for Secure Generation of Code

**Authors**: Ton, Khiem and Nguyen, Nhi and Nazzal, Mahmoud and Khreishah, Abdallah and Borcea, Cristian and Phan, NhatHai and Jin, Ruoming and Khalil, Issa and Shen, Yelong

**Abstract**:

This paper introduces SGCode, a flexible prompt-optimizing system to generate secure code with large language models (LLMs). SGCode integrates recent prompt-optimization approaches with LLMs in a unified system accessible through front-end and back-end APIs, enabling users to 1) generate secure code, which is free of vulnerabilities, 2) review and share security analysis, and 3) easily switch from one prompt optimization approach to another, while providing insights on model and system performance. We populated SGCode on an AWS server with PromSec, an approach that optimizes prompts by combining an LLM and security tools with a lightweight generative adversarial graph neural network to detect and fix security vulnerabilities in the generated code. Extensive experiments show that SGCode is practical as a public tool to gain insights into the trade-offs between model utility, secure code generation, and system cost. SGCode has only a marginal cost compared with prompting LLMs. SGCode is available at: http://3.131.141.63:8501/.

**Link**: [Read Paper](https://doi.org/10.1145/3658644.3691367)

**Labels**: [code generation](../../labels/code_generation.md), [program synthesis](../../labels/program_synthesis.md), [agent design](../../labels/agent_design.md), [prompt strategy](../../labels/prompt_strategy.md), [code model](../../labels/code_model.md), [code model security](../../labels/code_model_security.md)
