# NAACL2025

Number of papers: 13

## [Benchmarking Language Model Creativity: A Case Study on Code Generation](paper_4.md)
- **Authors**: Lu, Yining  and      Wang, Dixuan  and      Li, Tianjian  and      Jiang, Dongwei  and      Khudanpur, Sanjeev  and      Jiang, Meng  and      Khashabi, Daniel
- **Abstract**: As LLMs become increasingly prevalent, it is interesting to consider how ``creative'' these models can be. From cognitive science, creativity consists of at least two key characteristics: \textit{convergent} thinking (purposefulness to achieve a given goal) and \textit{divergent} thinking (adaptability to explore new environments or constraints) (CITATION). In this work, we introduce a framework for quantifying LLM creativity that incorporates the two design ingredients: (1) We introduce DENIAL ...
- **Link**: [Read Paper](https://aclanthology.org/2025.naacl-long.141/)
- **Labels**: [code generation](../../labels/code_generation.md), [program synthesis](../../labels/program_synthesis.md), [benchmark](../../labels/benchmark.md)


## [Few-Shot Natural Language to First-Order Logic Translation via Code Generation](paper_9.md)
- **Authors**: Liu, Junnan
- **Abstract**: Translation of natural language to first-order logical formula (NL-FOL) has recently gained significant attention for its critical role in logic-based NLP applications. Some studies attempt to utilize pretrained language models in a sequence-to-sequence manner for the NL-FOL task. However, these methods encounter challenges such as (1) inconsistency between the training and inference phases and (2) the data-intensive and resource-intensive finetuning process. This paper introduces a novel NL-FOL...
- **Link**: [Read Paper](https://aclanthology.org/2025.naacl-long.547/)
- **Labels**: [code generation](../../labels/code_generation.md), [program synthesis](../../labels/program_synthesis.md)


## [Investigating the Transferability of Code Repair for Low-Resource Programming Languages](paper_2.md)
- **Authors**: Wong, Kyle  and      Amayuelas, Alfonso  and      Pan, Liangming  and      Wang, William Yang
- **Abstract**: Large language models (LLMs) have shown remarkable performance on code generation tasks. A recent use case is iterative code repair, where an LLM fixes an incorrect program by rationalizing about errors and generating new code. Recent works augment the code repair process by integrating modern techniques such as chain-of-thought reasoning or distillation, but only study their benefits on high-resource languages like Python, and ignore low-resource languages like Perl. To address this gap of know...
- **Link**: [Read Paper](https://aclanthology.org/2025.findings-naacl.190/)
- **Labels**: [code generation](../../labels/code_generation.md), [program repair](../../labels/program_repair.md), [empirical study](../../labels/empirical_study.md)


## [Mastering the Craft of Data Synthesis for {C}ode{LLM}s](paper_10.md)
- **Authors**: Chen, Meng  and      Arthur, Philip  and      Feng, Qianyu  and      Hoang, Cong Duy Vu  and      Hong, Yu-Heng  and      Moghaddam, Mahdi Kazemi  and      Nezami, Omid  and      Nguyen, Duc Thien  and      Tangari, Gioacchino  and      Vu, Duy  and      Vu, Thanh  and      Johnson, Mark  and      Kenthapadi, Krishnaram  and      Dharmasiri, Don  and      Duong, Long  and      Li, Yuan-Fang
- **Abstract**: Large language models (LLMs) have shown impressive performance in \textit{code} understanding and generation, making coding tasks a key focus for researchers due to their practical applications and value as a testbed for LLM evaluation. Data synthesis and filtering techniques have been widely adopted and shown to be highly effective in this context. In this paper, we present a focused survey and taxonomy of these techniques, emphasizing recent advancements. We highlight key challenges, explore f...
- **Link**: [Read Paper](https://aclanthology.org/2025.naacl-long.620/)
- **Labels**: [general coding task](../../labels/general_coding_task.md), [empirical study](../../labels/empirical_study.md)


## [On the Impacts of Contexts on Repository-Level Code Generation](paper_11.md)
- **Authors**: Hai, Nam Le  and      Nguyen, Dung Manh  and      Bui, Nghi D. Q.
- **Abstract**: CodeLLMs are widely used for code generation, yet their ability to handle repository-level dependencies remains underexplored. We introduce RepoExec, a benchmark for evaluating repository-level code generation, focusing on executability, functional correctness, and dependency utilization. Our study evaluates 18 models, revealing that retaining full dependency context yields the best performance, while smaller context sizes can be misleading. Pretrained LLMs excel in correctness but often reimple...
- **Link**: [Read Paper](https://aclanthology.org/2025.findings-naacl.82/)
- **Labels**: [code generation](../../labels/code_generation.md), [program synthesis](../../labels/program_synthesis.md), [agent design](../../labels/agent_design.md), [prompt strategy](../../labels/prompt_strategy.md), [retrieval-augmented generation](../../labels/retrieval-augmented_generation.md)


## [What can Large Language Models Capture about Code Functional Equivalence?](paper_13.md)
- **Authors**: Maveli, Nickil  and      Vergari, Antonio  and      Cohen, Shay B
- **Abstract**: Code-LLMs, LLMs pre-trained on large code corpora, have shown great progress in learning rich representations of the structure and syntax of code, successfully using it to generate or classify code fragments. At the same time, understanding if they are able to do so because they capture code semantics, and how well, is still an open question. In this paper, we tackle this problem by introducing SeqCoBench, a benchmark for systematically assessing how Code-LLMs can capture code functional equival...
- **Link**: [Read Paper](https://aclanthology.org/2025.findings-naacl.382/)
- **Labels**: [static analysis](../../labels/static_analysis.md), [equivalence checking](../../labels/equivalence_checking.md), [empirical study](../../labels/empirical_study.md), [benchmark](../../labels/benchmark.md)


## [{COAST}: Enhancing the Code Debugging Ability of {LLM}s through Communicative Agent Based Data Synthesis](paper_12.md)
- **Authors**: Yang, Weiqing  and      Wang, Hanbin  and      Liu, Zhenghao  and      Li, Xinze  and      Yan, Yukun  and      Wang, Shuo  and      Gu, Yu  and      Yu, Minghe  and      Liu, Zhiyuan  and      Yu, Ge
- **Abstract**: Code debugging is a vital stage of software development, essential for ensuring the reliability and performance of Large Language Models (LLMs) in the code generation task. Human debugging typically follows a multi-stage process, which includes Bug Localization, Bug Identification, Code Repair, and Code Recognition. However, existing code debugging benchmarks predominantly focus on the Code Repair stage, which offers only a limited perspective on evaluating the debugging capabilities of LLMs. In...
- **Link**: [Read Paper](https://aclanthology.org/2025.findings-naacl.139/)
- **Labels**: [program testing](../../labels/program_testing.md), [debugging](../../labels/debugging.md), [agent design](../../labels/agent_design.md), [code model](../../labels/code_model.md), [code model training](../../labels/code_model_training.md)


## [{CRS}core: Grounding Automated Evaluation of Code Review Comments in Code Claims and Smells](paper_7.md)
- **Authors**: Naik, Atharva  and      Alenius, Marcus  and      Fried, Daniel  and      Rose, Carolyn
- **Abstract**: The task of automated code review has recently gained a lot of attention from the machine learning community. However, current review comment evaluation metrics rely on comparisons with a human-written reference for a given code change (also called a diff ). Furthermore, code review is a one-to-many problem, like generation and summarization, with many ``valid reviews'' for a diff. Thus, we develop CRScore {---} a reference-free metric to measure dimensions of review quality like conciseness, co...
- **Link**: [Read Paper](https://aclanthology.org/2025.naacl-long.457/)
- **Labels**: [software maintenance and deployment](../../labels/software_maintenance_and_deployment.md), [code review](../../labels/code_review.md)


## [{C}odex{G}raph: Bridging Large Language Models and Code Repositories via Code Graph Databases](paper_3.md)
- **Authors**: Liu, Xiangyan  and      Lan, Bo  and      Hu, Zhiyuan  and      Liu, Yang  and      Zhang, Zhicheng  and      Wang, Fei  and      Shieh, Michael Qizhe  and      Zhou, Wenmeng
- **Abstract**: Large Language Models (LLMs) excel in stand-alone code tasks like HumanEval and MBPP, but struggle with handling entire code repositories. This challenge has prompted research on enhancing LLM-codebase interaction at a repository scale. Current solutions rely on similarity-based retrieval or manual tools and APIs, each with notable drawbacks. Similarity-based retrieval often has low recall in complex tasks, while manual tools and APIs are typically task-specific and require expert knowledge, red...
- **Link**: [Read Paper](https://aclanthology.org/2025.naacl-long.7/)
- **Labels**: [agent design](../../labels/agent_design.md), [prompt strategy](../../labels/prompt_strategy.md), [retrieval-augmented generation](../../labels/retrieval-augmented_generation.md)


## [{C}ode{T}ree: Agent-guided Tree Search for Code Generation with Large Language Models](paper_5.md)
- **Authors**: Li, Jierui  and      Le, Hung  and      Zhou, Yingbo  and      Xiong, Caiming  and      Savarese, Silvio  and      Sahoo, Doyen
- **Abstract**: Pretrained on massive amounts of code and text data, large language models (LLMs) have demonstrated remarkable achievements in performing code generation tasks. With additional execution-based feedback, these models can act as agents with capabilities to self-refine and improve generated code autonomously. However, on challenging coding tasks with extremely large search space, current agentic approaches still struggle with multi-stage planning, generating, and debugging. To address this problem,...
- **Link**: [Read Paper](https://aclanthology.org/2025.naacl-long.189/)
- **Labels**: [code generation](../../labels/code_generation.md), [program synthesis](../../labels/program_synthesis.md), [agent design](../../labels/agent_design.md), [planning](../../labels/planning.md)


## [{DCE}-{LLM}: Dead Code Elimination with Large Language Models](paper_8.md)
- **Authors**: Chen, Minyu  and      Li, Guoqiang  and      Wu, Ling-I  and      Liu, Ruibang
- **Abstract**: Dead code introduces several challenges in software development, such as increased binary size and maintenance difficulties. It can also obscure logical errors and be exploited for obfuscation in malware. For LLM-based code-related tasks, dead code introduces vulnerabilities that can mislead these models, raising security concerns. Although modern compilers and IDEs offer dead code elimination, sophisticated patterns can bypass these tools. A universal approach that includes classification, loca...
- **Link**: [Read Paper](https://aclanthology.org/2025.naacl-long.501/)
- **Labels**: [static analysis](../../labels/static_analysis.md), [bug detection](../../labels/bug_detection.md), [program optimization](../../labels/program_optimization.md)


## [{D}esign2{C}ode: Benchmarking Multimodal Code Generation for Automated Front-End Engineering](paper_6.md)
- **Authors**: Si, Chenglei  and      Zhang, Yanzhe  and      Li, Ryan  and      Yang, Zhengyuan  and      Liu, Ruibo  and      Yang, Diyi
- **Abstract**: Generative AI has made rapid advancements in recent years, achieving unprecedented capabilities in multimodal understanding and code generation. This can enable a new paradigm of front-end development in which multimodal large language models (MLLMs) directly convert visual designs into code implementations. In this work, we construct Design2Code {--} the first real-world benchmark for this task. Specifically, we manually curate 484 diverse real-world webpages as test cases and develop a set of ...
- **Link**: [Read Paper](https://aclanthology.org/2025.naacl-long.199/)
- **Labels**: [code generation](../../labels/code_generation.md), [program synthesis](../../labels/program_synthesis.md), [benchmark](../../labels/benchmark.md)


## [{PLEX}: Adaptive Parameter-Efficient Fine-Tuning for Code {LLM}s using Lottery-Tickets](paper_1.md)
- **Authors**: Lee, Jaeseong  and    Han, Hojae  and    Kim, Jongyoon  and    Hwang, Seung-won  and    Kang, Naun  and    An, KyungJun  and    Jang, Sungho
- **Abstract**: Fine-tuning large language models (LLMs) for code generation is challenging due to computational costs and the underrepresentation of some programming languages (PLs) in pre-training. We propose PLEX, a lottery-ticket based parameter-efficient fine-tuning (PEFT) method that adapts LLMs to either well-supported and underrepresented PLs.During lottery ticket selection, PLEX employs a dual strategy: for well-represented PLs, it leverages the LLM{'}s full parametric knowledge by selecting from full ...
- **Link**: [Read Paper](https://aclanthology.org/2025.naacl-industry.60/)
- **Labels**: [code generation](../../labels/code_generation.md), [program synthesis](../../labels/program_synthesis.md), [code model](../../labels/code_model.md), [code model training](../../labels/code_model_training.md)
