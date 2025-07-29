# ISSTA2025

Number of papers: 33

## [A Large-Scale Empirical Study on Fine-Tuning Large Language Models for Unit Testing](paper_26.md)
- **Authors**: Shang, Ye and Zhang, Quanjun and Fang, Chunrong and Gu, Siqi and Zhou, Jianyi and Chen, Zhenyu
- **Abstract**: Unit testing plays a pivotal role in software development, improving software quality and reliability. However, generating effective test cases manually is time-consuming, prompting interest in unit testing research.   Recently, Large Language Models (LLMs) have shown potential in various unit testing tasks, including test generation, assertion generation, and test evolution, but existing studies are limited in scope and lack a systematic evaluation of the effectiveness of LLMs.    To bridge thi...
- **Link**: [Read Paper](https://doi.org/10.1145/3728951)
- **Labels**: [program testing](../../labels/program_testing.md), [unit testing](../../labels/unit_testing.md), [empirical study](../../labels/empirical_study.md)


## [AdverIntent-Agent: Adversarial Reasoning for Repair Based on Inferred Program Intent](paper_18.md)
- **Authors**: Ye, He and Yang, Aidan Z.H. and Hu, Chang and Wang, Yanlin and Zhang, Tao and Le Goues, Claire
- **Abstract**: Automated program repair (APR) has shown promising results, particularly with the use of neural networks. Currently, most APR tools focus on code transformations specified by test suites, rather than reasoning about the program’s intent and the high-level bug specification. Without a proper understanding of program intent, these tools tend to generate patches that overfit incomplete test suites and fail to reflect the developer’s intentions. However, reasoning about program intent is challenging...
- **Link**: [Read Paper](https://doi.org/10.1145/3728939)
- **Labels**: [code generation](../../labels/code_generation.md), [program repair](../../labels/program_repair.md), [static analysis](../../labels/static_analysis.md), [specification inference](../../labels/specification_inference.md)


## [Beyond Static Pattern Matching? Rethinking Automatic Cryptographic API Misuse Detection in the Era of LLMs](paper_3.md)
- **Authors**: Xia, Yifan and Xie, Zichen and Liu, Peiyu and Lu, Kangjie and Liu, Yan and Wang, Wenhai and Ji, Shouling
- **Abstract**: While the automated detection of cryptographic API misuses has progressed significantly, its precision diminishes for intricate targets due to the reliance on manually defined patterns. Large Language Models (LLMs) offer a promising context-aware understanding to address this shortcoming, yet the stochastic nature and the hallucination issue pose challenges to their applications in precise security analysis. This paper presents the first systematic study to explore LLMs’ application in cryptogra...
- **Link**: [Read Paper](https://doi.org/10.1145/3728875)
- **Labels**: [static analysis](../../labels/static_analysis.md), [bug detection](../../labels/bug_detection.md)


## [BinQuery: A Novel Framework for Natural Language-Based Binary Code Retrieval](paper_15.md)
- **Authors**: Zhang, Bolun and Gao, Zeyu and Wang, Hao and Cui, Yuxin and Qin, Siliang and Zhang, Chao and Chen, Kai and Zhao, Beibei
- **Abstract**: Binary Function Retrieval (BFR) is crucial in reverse engineering for identifying specific functions in binary code, especially those associated with malicious behavior or vulnerabilities. Traditional BFR methods rely on heuristics, often lacking the efficiency and adaptability needed for large-scale or diverse binary analysis tasks. To address these challenges, we present BinQuery, a Natural Language-based BFR (NL-based BFR) framework that uses natural language queries to retrieve relevant bina...
- **Link**: [Read Paper](https://doi.org/10.1145/3728927)
- **Labels**: [static analysis](../../labels/static_analysis.md), [code search](../../labels/code_search.md), [code summarization](../../labels/code_summarization.md)


## [Can LLMs Replace Human Evaluators? An Empirical Study of LLM-as-a-Judge in Software Engineering](paper_30.md)
- **Authors**: Wang, Ruiqi and Guo, Jiyu and Gao, Cuiyun and Fan, Guodong and Chong, Chun Yong and Xia, Xin
- **Abstract**: Recently, large language models (LLMs) have been deployed to tackle various software engineering (SE) tasks like code generation, significantly advancing the automation of SE tasks. However, assessing the quality of these LLM-generated code and text remains challenging. The commonly used Pass@k metric necessitates extensive unit tests and configured environments, demands a high labor cost, and is not suitable for evaluating LLM-generated text. Conventional metrics like BLEU, which measure only l...
- **Link**: [Read Paper](https://doi.org/10.1145/3728963)
- **Labels**: [software maintenance and deployment](../../labels/software_maintenance_and_deployment.md), [code review](../../labels/code_review.md), [empirical study](../../labels/empirical_study.md)


## [Causality-Aided Evaluation and Explanation of Large Language Model-Based Code Generation](paper_17.md)
- **Authors**: Ji, Zhenlan and Ma, Pingchuan and Li, Zongjie and Wang, Zhaoyu and Wang, Shuai
- **Abstract**: While code generation has been widely used in various software development scenarios, the quality of the generated code is not guaranteed. This has been a particular concern in the era of large language models (LLM)-based code generation, where LLMs, deemed a complex and powerful black-box model, are instructed by a high-level natural language specification, namely a prompt, to generate code. Nevertheless, effectively evaluating and explaining the code generation capability of LLMs is inherently...
- **Link**: [Read Paper](https://doi.org/10.1145/3728938)
- **Labels**: [code generation](../../labels/code_generation.md), [program synthesis](../../labels/program_synthesis.md)


## [ClassEval-T: Evaluating Large Language Models in Class-Level Code Translation](paper_19.md)
- **Authors**: Xue, Pengyu and Wu, Linhao and Yang, Zhen and Wang, Chengyi and Li, Xiang and Zhang, Yuxiang and Li, Jia and Jin, Ruikai and Pei, Yifei and Shen, Zhaoyan and Lyu, Xiran and Keung, Jacky Wai
- **Abstract**: In recent years, Large Language Models (LLMs) have dramatically advanced the performance of automated code translation, making their computational accuracy score reach up to over 80\% on many previous benchmarks. However, most code samples in these benchmarks are short, standalone, statement/method-level, and algorithmic, which is not aligned with practical coding tasks. Therefore, it is still unknown the actual capability of LLMs in translating code samples written for daily development.    To ...
- **Link**: [Read Paper](https://doi.org/10.1145/3728940)
- **Labels**: [code generation](../../labels/code_generation.md), [program transformation](../../labels/program_transformation.md)


## [Clause2Inv: A Generate-Combine-Check Framework for Loop Invariant Inference](paper_13.md)
- **Authors**: Cao, Weining and Wu, Guangyuan and Xu, Tangzhi and Yao, Yuan and Wei, Hengfeng and Chen, Taolue and Ma, Xiaoxing
- **Abstract**: Loop invariant inference is a fundamental, yet challenging, problem in program verification. Recent work adopts the guess-and-check framework, where candidate loop invariants are iteratively generated in the guess step and verified in the check step. A major challenge of this general framework is to produce high-quality candidate invariants in each iteration so that the inference procedure can converge quickly. Empirically, we observe that existing approaches may struggle with guessing the compl...
- **Link**: [Read Paper](https://doi.org/10.1145/3728920)
- **Labels**: [static analysis](../../labels/static_analysis.md), [program verification](../../labels/program_verification.md)


## [ConTested: Consistency-Aided Tested Code Generation with LLM](paper_8.md)
- **Authors**: Dong, Jinhao and Sun, Jun and Zhang, Wenjie and Dong, Jin Song and Hao, Dan
- **Abstract**: Recent advancements in large language models (LLMs) have significantly improved code generation, which generates code snippets automatically based on natural language requirements. Despite achieving state-of-the-art performance, LLMs often struggle to generate accurate and reliable code, requiring developers to spend substantial effort debugging and evaluating the generated output. Researchers have proposed leveraging Consistency to select code that passes more tests (inter-consistency) and demo...
- **Link**: [Read Paper](https://doi.org/10.1145/3728902)
- **Labels**: [code generation](../../labels/code_generation.md), [program synthesis](../../labels/program_synthesis.md), [program testing](../../labels/program_testing.md)


## [CrossProbe: LLM-Empowered Cross-Project Bug Detection for Deep Learning Frameworks](paper_33.md)
- **Authors**: Guan, Hao and Bai, Guangdong and Liu, Yepang
- **Abstract**: Deep Learning (DL) models may introduce reliability challenges in the underlying DL frameworks. These frameworks may be prone to bugs that can lead to crash or wrong results, particularly when involving complex model architectures and substantial computational demands. Such framework bugs can disrupt DL applications, impacting customer experience and potentially causing financial losses. Traditional approaches to testing DL frameworks face limitations in adapting to the vast search space of mode...
- **Link**: [Read Paper](https://doi.org/10.1145/3728984)
- **Labels**: [program testing](../../labels/program_testing.md), [library testing](../../labels/library_testing.md)


## [DecLLM: LLM-Augmented Recompilable Decompilation for Enabling Programmatic Use of Decompiled Code](paper_27.md)
- **Authors**: Wong, Wai Kin and Wu, Daoyuan and Wang, Huaijin and Li, Zongjie and Liu, Zhibo and Wang, Shuai and Tang, Qiyi and Nie, Sen and Wu, Shi
- **Abstract**: Decompilers are widely used in reverse engineering (RE) to convert compiled executables into human-readable pseudocode and support various security analysis tasks. Existing decompilers, such as IDA Pro and Ghidra, focus on enhancing the readability of decompiled code rather than its recompilability, which limits further programmatic use, such as for CodeQL-based vulnerability analysis that requires compilable versions of the decompiled code. Recent LLM-based approaches for enhancing decompilatio...
- **Link**: [Read Paper](https://doi.org/10.1145/3728958)
- **Labels**: [code generation](../../labels/code_generation.md), [program decompilation](../../labels/program_decompilation.md)


## [Enhanced Prompting Framework for Code Summarization with Large Language Models](paper_25.md)
- **Authors**: Fang, Minying and Yuan, Xing and Li, Yuying and Li, Haojie and Fang, Chunrong and Du, Junwei
- **Abstract**: Code summarization is essential for enhancing the efficiency of software development, enabling developers to swiftly comprehend and maintain software projects. Recent efforts utilizing large language models for generating precise code summaries have shown promising performance, primarily due to their advanced generative capabilities. LLMs that employ continuous prompting techniques can explore a broader problem space, potentially unlocking greater capabilities. However, they also present specifi...
- **Link**: [Read Paper](https://doi.org/10.1145/3728949)
- **Labels**: [static analysis](../../labels/static_analysis.md), [code summarization](../../labels/code_summarization.md)


## [Enhancing Vulnerability Detection via Inter-procedural Semantic Completion](paper_11.md)
- **Authors**: Wu, Bozhi and Liu, Chengjie and Li, Zhiming and Cao, Yushi and Sun, Jun and Lin, Shang-Wei
- **Abstract**: Inspired by advances in deep learning, numerous learning-based approaches for vulnerability detection have emerged, primarily operating at the function level for scalability. However, this design choice has a critical limitation: many vulnerabilities span multiple functions, causing function-level approaches to lose the semantics of called functions and fail to capture true vulnerability patterns. To address this issue, we propose VulnSC, a novel framework designed to enhance learning-based appr...
- **Link**: [Read Paper](https://doi.org/10.1145/3728912)
- **Labels**: [static analysis](../../labels/static_analysis.md), [bug detection](../../labels/bug_detection.md), [code summarization](../../labels/code_summarization.md)


## [Identifying Multi-parameter Constraint Errors in Python Data Science Library API Documentation](paper_22.md)
- **Authors**: Xu, Xiufeng and Xie, Fuman and Zhu, Chenguang and Bai, Guangdong and Khurshid, Sarfraz and Li, Yi
- **Abstract**: Modern AI- and Data-intensive software systems rely heavily on data science and machine learning libraries that provide essential algorithmic implementations and computational frameworks. These libraries expose complex APIs whose correct usage has to follow constraints among multiple interdependent parameters. Developers using these APIs are expected to learn about the constraints through the provided documentation and any discrepancy may lead to unexpected behaviors. However, maintaining correc...
- **Link**: [Read Paper](https://doi.org/10.1145/3728945)
- **Labels**: [static analysis](../../labels/static_analysis.md), [bug detection](../../labels/bug_detection.md)


## [KEENHash: Hashing Programs into Function-Aware Embeddings for Large-Scale Binary Code Similarity Analysis](paper_10.md)
- **Authors**: Liu, Zhijie and Tang, Qiyi and Nie, Sen and Wu, Shi and Zhang, Liang Feng and Tang, Yutian
- **Abstract**: Binary code similarity analysis (BCSA) is a crucial research area in many fields such as cybersecurity. Specifically, function-level diffing tools are the most widely used in BCSA: they perform function matching one by one for evaluating the similarity between binary programs. However, such methods need a high time complexity, making them unscalable in large-scale scenarios (e.g., 1/n-to-n search). Towards effective and efficient program-level BCSA, we propose KEENHash, a novel hashing approach ...
- **Link**: [Read Paper](https://doi.org/10.1145/3728911)
- **Labels**: [static analysis](../../labels/static_analysis.md), [code similarity analysis](../../labels/code_similarity_analysis.md)


## [LLM Hallucinations in Practical Code Generation: Phenomena, Mechanism, and Mitigation](paper_7.md)
- **Authors**: Zhang, Ziyao and Wang, Chong and Wang, Yanlin and Shi, Ensheng and Ma, Yuchi and Zhong, Wanjun and Chen, Jiachi and Mao, Mingzhi and Zheng, Zibin
- **Abstract**: Code generation aims to automatically generate code from input requirements, significantly enhancing development efficiency. Recent large language models (LLMs) based approaches have shown promising results and revolutionized code generation task. Despite the promising performance, LLMs often generate contents with hallucinations, especially for the code generation scenario requiring the handling of complex contextual dependencies in practical development process. Although previous study has ana...
- **Link**: [Read Paper](https://doi.org/10.1145/3728894)
- **Labels**: [code generation](../../labels/code_generation.md), [hallucination in reasoning](../../labels/hallucination_in_reasoning.md), [empirical study](../../labels/empirical_study.md)


## [LLM4SZZ: Enhancing SZZ Algorithm with Context-Enhanced Assessment on Large Language Models](paper_5.md)
- **Authors**: Tang, Lingxiao and Liu, Jiakun and Liu, Zhongxin and Yang, Xiaohu and Bao, Lingfeng
- **Abstract**: The SZZ algorithm is the dominant technique for identifying bug-inducing commits and serves as a foundation for many software engineering studies, such as bug prediction and static code analysis, thereby enhancing software quality and facilitating better maintenance practices. Researchers have proposed many variants to enhance the SZZalgorithm’s performance since its introduction. The majority of them rely on static techniques or heuristic assumptions, making them easy to implement, but their pe...
- **Link**: [Read Paper](https://doi.org/10.1145/3728885)
- **Labels**: [software maintenance and deployment](../../labels/software_maintenance_and_deployment.md), [empirical study](../../labels/empirical_study.md)


## [MLLM-Based UI2Code Automation Guided by UI Layout Information](paper_14.md)
- **Authors**: Wu, Fan and Gao, Cuiyun and Li, Shuqing and Wen, Xin-Cheng and Liao, Qing
- **Abstract**: Converting user interfaces into code (UI2Code) is a crucial step in website development, which is time-consuming and labor-intensive. The automation of UI2Code is essential to streamline this task, beneficial for improving the development efficiency. There exist deep learning-based methods for the task; however, they heavily rely on a large amount of labeled training data and struggle with generalizing to real-world, unseen web page designs. The advent of Multimodal Large Language Models (MLLMs)...
- **Link**: [Read Paper](https://doi.org/10.1145/3728925)
- **Labels**: [code generation](../../labels/code_generation.md), [program synthesis](../../labels/program_synthesis.md)


## [OmniGIRL: A Multilingual and Multimodal Benchmark for GitHub Issue Resolution](paper_2.md)
- **Authors**: Guo, Lianghong and Tao, Wei and Jiang, Runhan and Wang, Yanlin and Chen, Jiachi and Liu, Xilin and Ma, Yuchi and Mao, Mingzhi and Zhang, Hongyu and Zheng, Zibin
- **Abstract**: The GitHub issue resolution task aims to resolve issues reported in repositories automatically. With advances in large language models (LLMs), this task has gained increasing attention, and several benchmarks are proposed to evaluate the issue resolution ability of LLMs. However, existing benchmarks have three main limitations. First, current benchmarks focus on a single programming language, limiting the evaluation of issues from repositories across different languages. Second, they usually cov...
- **Link**: [Read Paper](https://doi.org/10.1145/3728871)
- **Labels**: [code generation](../../labels/code_generation.md), [program repair](../../labels/program_repair.md)


## [OpDiffer: LLM-Assisted Opcode-Level Differential Testing of Ethereum Virtual Machine](paper_23.md)
- **Authors**: Ma, Jie and He, Ningyu and Xi, Jinwen and Xing, Mingzhe and Wang, Haoyu and Gao, Ying and Yue, Yinliang
- **Abstract**: As Ethereum continues to thrive, the Ethereum Virtual Machine (EVM) has become the cornerstone powering tens of millions of active smart contracts. Intuitively, security issues in EVMs could lead to inconsistent behaviors among smart contracts or even denial-of-service of the entire blockchain network. However, to the best of our knowledge, only a limited number of studies focus on the security of EVMs. Moreover, they suffer from 1) insufficient test input diversity and invalid semantics; and 2)...
- **Link**: [Read Paper](https://doi.org/10.1145/3728946)
- **Labels**: [program testing](../../labels/program_testing.md), [differential testing](../../labels/differential_testing.md)


## [PatchScope: LLM-Enhanced Fine-Grained Stable Patch Classification for Linux Kernel](paper_21.md)
- **Authors**: Liu, Rongkai and Shi, Heyuan and Liu, Shuning and Hu, Chao and Li, Sisheng and Shen, Yuheng and Wang, Runzhe and Shi, Xiaohai and Jiang, Yu
- **Abstract**: Stable patch classification plays a crucial role in vulnerability management for the Linux kernel, significantly contributing to the stability and security of Long-term support(LTS) versions. Although existing tools have effectively assisted in assessing whether patches should be merged into stable versions, they cannot determine which stable patches should be merged into which LTS versions. This process still requires the maintainers of the distribution community to manually screen based on the...
- **Link**: [Read Paper](https://doi.org/10.1145/3728944)
- **Labels**: [software maintenance and deployment](../../labels/software_maintenance_and_deployment.md), [code review](../../labels/code_review.md)


## [Porting Software Libraries to OpenHarmony: Transitioning from TypeScript or JavaScript to ArkTS](paper_20.md)
- **Authors**: Zhou, Bo and Shi, Jiaqi and Wang, Ying and Li, Li and Li, Tsz On and Yu, Hai and Zhu, Zhiliang
- **Abstract**: OpenHarmony emerges as a potent force in the mobile app domain, poised to stand alongside established industry giants. ArkTS is its main language, enhancing TypeScript (TS) and JavaScript (JS) with strict typing for improved performance. Developers are encouraged to port popular TS/JS libraries to OpenHarmony, supported by detailed guidelines. However, this requires a deep understanding of ArkTS syntax, following porting specifications, and making manual changes. An automated solution is crucial...
- **Link**: [Read Paper](https://doi.org/10.1145/3728941)
- **Labels**: [code generation](../../labels/code_generation.md), [program transformation](../../labels/program_transformation.md)


## [REACCEPT: Automated Co-evolution of Production and Test Code Based on Dynamic Validation and Large Language Models](paper_16.md)
- **Authors**: Chi, Jianlei and Wang, Xiaotian and Huang, Yuhan and Yu, Lechen and Cui, Di and Sun, Jianguo and Sun, Jun
- **Abstract**: Synchronizing production and test code, known as PT co-evolution, is critical for software quality. Given the significant manual effort involved, researchers have tried automating PT co-evolution using predefined heuristics and machine learning models. However, existing solutions are still incomplete. Most approaches only detect and flag obsolete test cases, leaving developers to manually update them. Meanwhile, existing solutions may suffer from low accuracy, especially when applied to real-wor...
- **Link**: [Read Paper](https://doi.org/10.1145/3728930)
- **Labels**: [program testing](../../labels/program_testing.md), [code generation](../../labels/code_generation.md)


## [Robust Vulnerability Detection across Compilations: LLVM-IR vs. Assembly with Transformer Model](paper_9.md)
- **Authors**: Shir, Rony and Surve, Priyanka and Elovici, Yuval and Shabtai, Asaf
- **Abstract**: Detecting vulnerabilities in binary files is a challenging task in cybersecurity, particularly when source code is unavailable and the compilation process and its parameters are unknown. Existing deep learning-based detection methods often rely on knowing a binary’s specific compilation settings, which may limit their ability to perform well on other types of binaries. In this research, we provide a thorough comparison of assembly representation and LLVM-IR to identify which representation is mo...
- **Link**: [Read Paper](https://doi.org/10.1145/3728903)
- **Labels**: [static analysis](../../labels/static_analysis.md), [bug detection](../../labels/bug_detection.md), [code model](../../labels/code_model.md), [code model robustness](../../labels/code_model_robustness.md)


## [STRUT: Structured Seed Case Guided Unit Test Generation for C Programs using LLMs](paper_31.md)
- **Authors**: Liu, Jinwei and Li, Chao and Chen, Rui and Li, Shaofeng and Gu, Bin and Yang, Mengfei
- **Abstract**: Unit testing plays a crucial role in bug detection and ensuring software correctness. It helps developers identify errors early in development, thereby reducing software defects. In recent years, large language models (LLMs) have demonstrated significant potential in automating unit test generation. However, using LLMs to generate unit tests faces many challenges. 1) The execution pass rate of the test cases generated by LLMs is low. 2) The test case coverage is inadequate, making it challenging...
- **Link**: [Read Paper](https://doi.org/10.1145/3728970)
- **Labels**: [program testing](../../labels/program_testing.md), [unit testing](../../labels/unit_testing.md)


## [SWE-GPT: A Process-Centric Language Model for Automated Software Improvement](paper_32.md)
- **Authors**: Ma, Yingwei and Cao, Rongyu and Cao, Yongchang and Zhang, Yue and Chen, Jue and Liu, Yibo and Liu, Yuchen and Li, Binhua and Huang, Fei and Li, Yongbin
- **Abstract**: Large language models (LLMs) have demonstrated remarkable performance in code generation, significantly enhancing the coding efficiency of developers. Recent advancements in LLM-based agents have led to significant progress in end-to-end automatic software engineering (ASE), particularly in software maintenance (e.g., fixing software issues) and evolution (e.g., adding new features). Despite these encouraging advances, current research faces two major challenges. First, state-of-the-art performa...
- **Link**: [Read Paper](https://doi.org/10.1145/3728981)
- **Labels**: [general coding task](../../labels/general_coding_task.md), [code generation](../../labels/code_generation.md), [program synthesis](../../labels/program_synthesis.md), [software maintenance and deployment](../../labels/software_maintenance_and_deployment.md), [agent design](../../labels/agent_design.md)


## [Safe4U: Identifying Unsound Safe Encapsulations of Unsafe Calls in Rust using LLMs](paper_6.md)
- **Authors**: Li, Huan and Wang, Bei and Hu, Xing and Xia, Xin
- **Abstract**: Rust is an emerging programming language that ensures safety through strict compile-time checks. A Rust function marked as unsafe indicates it has additional safety requirements (e.g., initialized, not null), known as contracts in the community. These unsafe functions can only be called within explicit unsafe blocks and the contracts must be guaranteed by the caller. To reuse and reduce unsafe code, the community recommends using safe encapsulation of unsafe calls (EUC) in practice. However, an ...
- **Link**: [Read Paper](https://doi.org/10.1145/3728890)
- **Labels**: [static analysis](../../labels/static_analysis.md), [bug detection](../../labels/bug_detection.md)


## [Smart-LLaMA-DPO: Reinforced Large Language Model for Explainable Smart Contract Vulnerability Detection](paper_4.md)
- **Authors**: Yu, Lei and Huang, Zhirong and Yuan, Hang and Cheng, Shiqi and Yang, Li and Zhang, Fengjun and Shen, Chenjie and Ma, Jiajia and Zhang, Jingyuan and Lu, Junyi and Zuo, Chun
- **Abstract**: Smart contract vulnerability detection is a critical challenge in the rapidly evolving blockchain landscape. Existing vulnerability detection methods face two main issues: (1) Existing datasets lack comprehensiveness and sufficient quality, with limited vulnerability type coverage and insufficient distinction between high-quality and low-quality explanations for preference learning. (2) Large language models (LLMs) often struggle with accurately interpreting specific concepts in smart contract s...
- **Link**: [Read Paper](https://doi.org/10.1145/3728878)
- **Labels**: [static analysis](../../labels/static_analysis.md), [bug detection](../../labels/bug_detection.md), [code model](../../labels/code_model.md), [code model training](../../labels/code_model_training.md), [source code model](../../labels/source_code_model.md)


## [The First Prompt Counts the Most! An Evaluation of Large Language Models on Iterative Example-Based Code Generation](paper_24.md)
- **Authors**: Fu, Yingjie and Li, Bozhou and Li, Linyi and Zhang, Wentao and Xie, Tao
- **Abstract**: The capabilities of Large Language Models (LLMs) in code generation have been extensively studied, particularly for implementing target functionalities from natural-language descriptions. As an alternative to natural language, input-output (I/O) examples provide an accessible, unambiguous, and flexible way to describe functionalities. However, their inherent diversity, opaqueness, and incompleteness impose greater challenges for understanding and implementing the target requirements. Therefore, ...
- **Link**: [Read Paper](https://doi.org/10.1145/3728947)
- **Labels**: [code generation](../../labels/code_generation.md), [program synthesis](../../labels/program_synthesis.md)


## [Tratto: A Neuro-Symbolic Approach to Deriving Axiomatic Test Oracles](paper_28.md)
- **Authors**: Molinelli, Davide and Martin-Lopez, Alberto and Zackrone, Elliott and Eken, Beyza and Ernst, Michael D. and Pezz\`{e}, Mauro
- **Abstract**: This paper presents Tratto, a neuro-symbolic approach that generates assertions (boolean expressions) that can serve as axiomatic oracles, from source code and documentation. The symbolic module of Tratto takes advantage of the grammar of the programming language, the unit under test, and the context of the unit (its class and available APIs) to restrict the search space of the tokens that can be successfully used to generate valid oracles. The neural module of Tratto uses transformers fine-tune...
- **Link**: [Read Paper](https://doi.org/10.1145/3728960)
- **Labels**: [program testing](../../labels/program_testing.md), [general testing](../../labels/general_testing.md)


## [Unlocking Low Frequency Syscalls in Kernel Fuzzing with Dependency-Based RAG](paper_12.md)
- **Authors**: Zhang, Zhiyu and Li, Longxing and Liang, Ruigang and Chen, Kai
- **Abstract**: Most coverage-guided kernel fuzzers test operating system kernels based on syscall sequence synthesis. However, there are still syscalls rarely or not covered (called low frequency syscalls, LFS) in a period of fuzzing, meaning the relevant code branches remain unexplored. This is due to the complex dependencies of the LFS and mutation uncertainty, which makes it difficult for fuzzers to generate corresponding syscall sequences. Since many kernel fuzzers can dynamically learn syscall dependencie...
- **Link**: [Read Paper](https://doi.org/10.1145/3728913)
- **Labels**: [program testing](../../labels/program_testing.md), [fuzzing](../../labels/fuzzing.md)


## [VerLog: Enhancing Release Note Generation for Android Apps using Large Language Models](paper_29.md)
- **Authors**: Guo, Jiawei and Yang, Haoran and Cai, Haipeng
- **Abstract**: Release notes are essential documents that communicate the details of software updates to users and developers, yet their generation remains a time-consuming and error-prone process. In this paper, we present VerLog, a novel technique that enhances the generation of software release notes using Large Language Models (LLMs). VerLog leverages few-shot in-context learning with adaptive prompting to facilitate the graph reasoning capabilities of LLMs, enabling them to accurately interpret and docume...
- **Link**: [Read Paper](https://doi.org/10.1145/3728961)
- **Labels**: [software maintenance and deployment](../../labels/software_maintenance_and_deployment.md), [documentation generation](../../labels/documentation_generation.md)


## [You Name It, I Run It: An LLM Agent to Execute Tests of Arbitrary Projects](paper_1.md)
- **Authors**: Bouzenia, Islem and Pradel, Michael
- **Abstract**: The ability to execute the test suite of a project is essential in many scenarios, e.g., to assess code quality and code coverage, to validate code changes made by developers or automated tools, and to ensure compatibility with dependencies. Despite its importance, executing the test suite of a project can be challenging in practice because different projects use different programming languages, software ecosystems, build systems, testing frameworks, and other tools. These challenges make it dif...
- **Link**: [Read Paper](https://doi.org/10.1145/3728922)
- **Labels**: [program testing](../../labels/program_testing.md), [general testing](../../labels/general_testing.md), [agent design](../../labels/agent_design.md)
