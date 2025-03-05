# CCS2024

Number of papers: 9

## [An Exploration of Large Language Models in Malicious Source Code Detection](paper_5.md)
- **Authors**: Xue, Di and Zhao, Gang and Fan, Zhongqi and Li, Wei and Xu, Yahong and Liu, Zhen and Liu, Yin and Yuan, Zhongliang
- **Abstract**: Embedding malicious code within the software supply chain has become a significant concern in the information technology field. Current methods for detecting malicious code, based on signatures, behavior analysis, and traditional machine learning models, lack result interpretability. This study proposes a novel malicious code detection framework, Mal-LLM, which leverages the cost advantages of traditional machine learning models and the interpretability of LLMs. Initially, traditional machine le...
- **Link**: [Read Paper](https://doi.org/10.1145/3658644.3691374)
- **Labels**: [static analysis](../../labels/static_analysis.md), [bug detection](../../labels/bug_detection.md)


## [Demystifying RCE Vulnerabilities in LLM-Integrated Apps](paper_3.md)
- **Authors**: Liu, Tong and Deng, Zizhuang and Meng, Guozhu and Li, Yuekang and Chen, Kai
- **Abstract**: Large Language Models (LLMs) show promise in transforming software development, with a growing interest in integrating them into more intelligent apps. Frameworks like LangChain aid LLM-integrated app development, offering code execution utility/APIs for custom actions. However, these capabilities theoretically introduce Remote Code Execution (RCE) vulnerabilities, enabling remote code execution through prompt injections. No prior research systematically investigates these frameworks' RCE vulner...
- **Link**: [Read Paper](https://doi.org/10.1145/3658644.3690338)
- **Labels**: [code model](../../labels/code_model.md), [code model security](../../labels/code_model_security.md)


## [Enhance Hardware Domain Specific Large Language Model with Reinforcement Learning for Resilience](paper_8.md)
- **Authors**: Fu, Weimin and Zhao, Yifang and Jin, Yier and Guo, Xiaolong
- **Abstract**: To enhance the performance of large language models (LLMs) on hardware design tasks, we focus on training with reinforcement learning(RL) to improve LLMs' syntax synthesis and functional verification performance. We observed significant gains in power, performance, and area (PPA) metrics by applying RL. Specifically, DeepSeek Code saw a 23.6\% performance increase, while the RTLCoder improved by 7.86\%. Our findings demonstrate the effectiveness of RL in refining LLMs for more accurate hardware ...
- **Link**: [Read Paper](https://doi.org/10.1145/3658644.3691384)
- **Labels**: [code generation](../../labels/code_generation.md), [program synthesis](../../labels/program_synthesis.md)


## [PromSec: Prompt Optimization for Secure Generation of Functional Source Code with Large Language Models (LLMs)](paper_4.md)
- **Authors**: Nazzal, Mahmoud and Khalil, Issa and Khreishah, Abdallah and Phan, NhatHai
- **Abstract**: The capability of generating high-quality source code using large language models (LLMs) reduces software development time and costs. However, recent literature and our empirical investigation in this work show that while LLMs can generate functioning code, they inherently tend to introduce security vulnerabilities, limiting their potential. This problem is mainly due to their training on massive open-source corpora exhibiting insecure and inefficient programming practices. Therefore, automatic ...
- **Link**: [Read Paper](https://doi.org/10.1145/3658644.3690298)
- **Labels**: [general coding task](../../labels/general_coding_task.md), [code generation](../../labels/code_generation.md), [code model](../../labels/code_model.md), [code model security](../../labels/code_model_security.md)


## [ProphetFuzz: Fully Automated Prediction and Fuzzing of High-Risk Option Combinations with Only Documentation via Large Language Model](paper_2.md)
- **Authors**: Wang, Dawei and Zhou, Geng and Chen, Li and Li, Dan and Miao, Yukai
- **Abstract**: Vulnerabilities related to option combinations pose a significant challenge in software security testing due to their vast search space. Previous research primarily addressed this challenge through mutation or filtering techniques, which inefficiently treated all option combinations as having equal potential for vulnerabilities, thus wasting considerable time on non-vulnerable targets and resulting in low testing efficiency. In this paper, we utilize carefully designed prompt engineering to driv...
- **Link**: [Read Paper](https://doi.org/10.1145/3658644.3690231)
- **Labels**: [program testing](../../labels/program_testing.md), [fuzzing](../../labels/fuzzing.md)


## [ReSym: Harnessing LLMs to Recover Variable and Data Structure Symbols from Stripped Binaries](paper_1.md)
- **Authors**: Xie, Danning and Zhang, Zhuo and Jiang, Nan and Xu, Xiangzhe and Tan, Lin and Zhang, Xiangyu
- **Abstract**: Decompilation aims to recover a binary executable to the source code form and hence has a wide range of applications in cyber security, such as malware analysis and legacy code hardening. A prominent challenge is to recover variable symbols, including both primitive and complex types such as user-defined data structures, along with their symbol information such as names and types. Existing efforts focus on solving parts of the problem, eg, recovering only types (without names) or only local vari...
- **Link**: [Read Paper](https://www.cs.purdue.edu/homes/lintan/publications/resym-ccs24.pdf)
- **Labels**: [code model](../../labels/code_model.md), [code model training](../../labels/code_model_training.md), [binary code model](../../labels/binary_code_model.md), [static analysis](../../labels/static_analysis.md), [program decompilation](../../labels/program_decompilation.md)


## [Repairing Bugs with the Introduction of New Variables: A Multi-Agent Large Language Model](paper_6.md)
- **Authors**: Zhang, Elisa and Sun, Shiyu and Xing, Yunlong and Sun, Kun
- **Abstract**: Trained on billions of tokens, large language models (LLMs) have a broad range of empirical knowledge which enables them to generate software patches with complex repair patterns. We leverage the powerful code-fixing capabilities of LLMs and propose VarPatch, a multi-agent conversational automated program repair (APR) technique that iteratively queries the LLM to generate software patches by providing various prompts and context information. VarPatch focuses on the variable addition repair patte...
- **Link**: [Read Paper](https://doi.org/10.1145/3658644.3691412)
- **Labels**: [code generation](../../labels/code_generation.md), [program repair](../../labels/program_repair.md)


## [SGCode: A Flexible Prompt-Optimizing System for Secure Generation of Code](paper_9.md)
- **Authors**: Ton, Khiem and Nguyen, Nhi and Nazzal, Mahmoud and Khreishah, Abdallah and Borcea, Cristian and Phan, NhatHai and Jin, Ruoming and Khalil, Issa and Shen, Yelong
- **Abstract**: This paper introduces SGCode, a flexible prompt-optimizing system to generate secure code with large language models (LLMs). SGCode integrates recent prompt-optimization approaches with LLMs in a unified system accessible through front-end and back-end APIs, enabling users to 1) generate secure code, which is free of vulnerabilities, 2) review and share security analysis, and 3) easily switch from one prompt optimization approach to another, while providing insights on model and system performan...
- **Link**: [Read Paper](https://doi.org/10.1145/3658644.3691367)
- **Labels**: [code generation](../../labels/code_generation.md), [program synthesis](../../labels/program_synthesis.md), [agent design](../../labels/agent_design.md), [prompt strategy](../../labels/prompt_strategy.md), [code model](../../labels/code_model.md), [code model security](../../labels/code_model_security.md)


## [TAPChecker: Model Checking in Trigger-Action Rules Generation Using Large Language Models](paper_7.md)
- **Authors**: Bui, Huan and Lienerth, Harper and Fu, Chenglong and Sridhar, Meera
- **Abstract**: The integration of large language models (LLMs) in smart home systems holds significant promise for automating the generation of Trigger-Action Programming (TAP) rules, potentially streamlining smart home user experiences and enhancing convenience. However, LLMs lack of holistic view of smart home IoT deployments and may introduce TAP rules that result in hazards. This paper explores the application of LLM for generating TAP rules and applying formal verification to validate and ensure the safet...
- **Link**: [Read Paper](https://doi.org/10.1145/3658644.3691416)
- **Labels**: [static analysis](../../labels/static_analysis.md), [specification inference](../../labels/specification_inference.md)
