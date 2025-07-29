# FSE2025

Number of papers: 42

## [A Knowledge Enhanced Large Language Model for Bug Localization](paper_25.md)
- **Authors**: Li, Yue and Liu, Bohan and Zhang, Ting and Wang, Zhiqi and Lo, David and Yang, Lanxin and Lyu, Jun and Zhang, He
- **Abstract**: A significant number of bug reports are generated every day as software systems continue to develop. Large Language Models (LLMs) have been used to correlate bug reports with source code to locate bugs automatically. The existing research has shown that LLMs are effective for bug localization and can increase software development efficiency. However, these studies still have two limitations. First, these models fail to capture context information about bug reports and source code. Second, these ...
- **Link**: [Read Paper](https://doi.org/10.1145/3729356)
- **Labels**: [program testing](../../labels/program_testing.md), [bug reproduction](../../labels/bug_reproduction.md)


## [Agentless: Demystifying LLM-based Software Engineering Agents](paper_2.md)
- **Authors**: Chunqiu Steven Xia, Yinlin Deng, Soren Dunn, Lingming Zhang
- **Abstract**: Recent advancements in large language models (LLMs) have significantly advanced the automation of software development tasks, including code synthesis, program repair, and test generation. More recently, researchers and industry practitioners have developed various autonomous LLM agents to perform end-to-end software development tasks. These agents are equipped with the ability to use tools, run commands, observe feedback from the environment, and plan for future actions. However, the complexity...
- **Link**: [Read Paper](https://arxiv.org/abs/2407.01489)
- **Labels**: [code generation](../../labels/code_generation.md), [program repair](../../labels/program_repair.md)


## [AlphaTrans: A Neuro-Symbolic Compositional Approach for Repository-Level Code Translation and Validation](paper_1.md)
- **Authors**: Ali Reza Ibrahimzada, Kaiyao Ke, Mrigank Pawagi, Muhammad Salman Abid, Rangeet Pan, Saurabh Sinha, Reyhaneh Jabbarvand
- **Abstract**: Code translation transforms programs from one programming language (PL) to another. Several rule-based transpilers have been designed to automate code translation between different pairs of PLs. However, the rules can become obsolete as the PLs evolve and cannot generalize to other PLs. Recent studies have explored the automation of code translation using Large Language Models (LLMs). One key observation is that such techniques may work well for crafted benchmarks but fail to generalize to the s...
- **Link**: [Read Paper](https://arxiv.org/pdf/2410.24117)
- **Labels**: [code generation](../../labels/code_generation.md), [program transformation](../../labels/program_transformation.md)


## [An Adaptive Language-Agnostic Pruning Method for Greener Language Models for Code](paper_17.md)
- **Authors**: Saad, Mootez and L\'{o}pez, Jos\'{e} Antonio Hern\'{a}ndez and Chen, Boqi and Varr\'{o}, D\'{a}niel and Sharma, Tushar
- **Abstract**: Language models of code have demonstrated remarkable performance across various software engineering and source code analysis tasks. However, their demanding computational resource requirements and consequential environmental footprint remain as significant challenges.               This work introduces ALPINE, an adaptive programming language-agnostic pruning technique designed to substantially reduce the computational overhead of these models.                The proposed method offers a plugga...
- **Link**: [Read Paper](https://doi.org/10.1145/3715773)
- **Labels**: [code model](../../labels/code_model.md), [code model training](../../labels/code_model_training.md)


## [Automated Unit Test Refactoring](paper_10.md)
- **Authors**: Gao, Yi and Hu, Xing and Yang, Xiaohu and Xia, Xin
- **Abstract**: Test smells arise from poor design practices and insufficient domain knowledge, which can lower the quality of test code and make it harder to maintain and update. Manually refactoring of test smells is time-consuming and error-prone, highlighting the necessity for automated approaches. Current rule-based refactoring methods often struggle in scenarios not covered by predefined rules and lack the flexibility needed to handle diverse cases effectively. In this paper, we propose a novel approach c...
- **Link**: [Read Paper](https://doi.org/10.1145/3715750)
- **Labels**: [program testing](../../labels/program_testing.md), [unit testing](../../labels/unit_testing.md), [code generation](../../labels/code_generation.md), [program transformation](../../labels/program_transformation.md)


## [Automatically Fixing Dependency Breaking Changes](paper_29.md)
- **Authors**: Fruntke, Lukas and Krinke, Jens
- **Abstract**: Breaking changes in dependencies are a common challenge in software development, requiring manual intervention to resolve. This study examines how well LLM automate the repair of breaking changes caused by dependency updates in Java projects. Although earlier methods have mostly concentrated on detecting breaking changes or investigating their impact, they have not been able to completely automate the repair process. We introduce and compare two new approaches: an agentic system that combines au...
- **Link**: [Read Paper](https://doi.org/10.1145/3729366)
- **Labels**: [code generation](../../labels/code_generation.md), [program repair](../../labels/program_repair.md)


## [Beyond Functional Correctness: Investigating Coding Style Inconsistencies in Large Language Models](paper_9.md)
- **Authors**: Wang, Yanlin and Jiang, Tianyue and Liu, Mingwei and Chen, Jiachi and Mao, Mingzhi and Liu, Xilin and Ma, Yuchi and Zheng, Zibin
- **Abstract**: Large language models (LLMs) have brought a paradigm shift to the field of code generation, offering the potential to enhance the software development process. However, previous research mainly focuses on the accuracy of code generation, while coding style differences between LLMs and human developers remain under-explored. In this paper, we empirically analyze the differences in coding style between the code generated by mainstream LLMs and the code written by human developers, and summarize co...
- **Link**: [Read Paper](https://doi.org/10.1145/3715749)
- **Labels**: [code generation](../../labels/code_generation.md), [empirical study](../../labels/empirical_study.md)


## [Beyond PEFT: Layer-Wise Optimization for More Effective and Efficient Large Code Model Tuning](paper_21.md)
- **Authors**: Wang, Chaozheng and Feng, Jia and Gao, Shuzheng and Gao, Cuiyun and Li, Zongjie and Peng, Ting and Huang, Hailiang and Deng, Yuetang and Lyu, Michael
- **Abstract**: Large Code Models (LCMs) have demonstrated remarkable effectiveness across various code intelligence tasks. Supervised fine-tuning is essential to optimize their performance for specific downstream tasks. Compared with the traditional full-parameter fine-tuning (FFT) method, Parameter-Efficient Fine-Tuning (PEFT) methods can train LCMs with substantially reduced resource consumption and have gained widespread attention among researchers and practitioners. While existing studies have explored PEF...
- **Link**: [Read Paper](https://doi.org/10.1145/3729341)
- **Labels**: [code model](../../labels/code_model.md), [code model training](../../labels/code_model_training.md)


## [Blended Analysis for Predictive Execution](paper_40.md)
- **Authors**: Li, Yi and Dhulipala, Hridya and Yadavally, Aashish and Rong, Xiaokai and Wang, Shaohua and Nguyen, Tien N.
- **Abstract**: Although Large Language Models (LLMs) are highly proficient in understanding source code and descriptive texts, they have limitations in reasoning on dynamic program behaviors, such as execution trace and code coverage prediction, and runtime error prediction, which usually require actual program execution. To advance the ability of LLMs in predicting dynamic behaviors, we leverage the strengths of both approaches, Program Analysis (PA) and LLM, in building PredEx, a predictive executor for Pyth...
- **Link**: [Read Paper](https://doi.org/10.1145/3729402)
- **Labels**: [program testing](../../labels/program_testing.md), [general testing](../../labels/general_testing.md)


## [Bridging Operator Semantic Inconsistencies: A Source-Level Cross-Framework Model Conversion Approach](paper_27.md)
- **Authors**: Li, Xingpei and Lei, Yan and Jia, Zhouyang and Zhang, Yuanliang and Liu, Haoran and Chen, Liqian and Dong, Wei and Li, Shanshan
- **Abstract**: As deep learning (DL) frameworks become widely used, converting models between frameworks is crucial for ecosystem flexibility. However, interestingly, existing model converters commonly focus on syntactic operator API mapping—transpiling operator names and parameters—which results in API compatibility issues (i.e., incompatible parameters, missing operators). These issues arise from semantic inconsistencies due to differences in operator implementation, causing conversion failure or performance...
- **Link**: [Read Paper](https://doi.org/10.1145/3729361)
- **Labels**: [code generation](../../labels/code_generation.md), [program transformation](../../labels/program_transformation.md), [empirical study](../../labels/empirical_study.md)


## [CKTyper: Enhancing Type Inference for Java Code Snippets by Leveraging Crowdsourcing Knowledge in Stack Overflow](paper_5.md)
- **Authors**: Li, Anji and Zhang, Neng and Zou, Ying and Chen, Zhixiang and Wang, Jian and Zheng, Zibin
- **Abstract**: Code snippets are widely used in technical forums to demonstrate solutions to programming problems. They can be leveraged by developers to accelerate problem-solving. However, code snippets often lack concrete types of the APIs used in them, which impedes their understanding and resue. To enhance the description of a code snippet, a number of approaches are proposed to infer the types of APIs. Although existing approaches can achieve good performance, their performance is limited by ignoring oth...
- **Link**: [Read Paper](https://doi.org/10.1145/3715724)
- **Labels**: [static analysis](../../labels/static_analysis.md), [type inference](../../labels/type_inference.md)


## [CRISPE: Semantic-Guided Execution Planning and Dynamic Reasoning for Enhancing Code Coverage Prediction](paper_39.md)
- **Authors**: Dhulipala, Hridya and Yadavally, Aashish and Patel, Smit Soneshbhai and Nguyen, Tien N.
- **Abstract**: While LLMs excel in understanding source code and descriptive texts for tasks like code generation, code completion, etc., they exhibit weaknesses in predicting dynamic program behavior, such as code coverage and runtime error detection, which typically require program execution. Aiming to advance the capability of LLMs in reasoning and predicting the program behavior at runtime, we present CRISPE (short for Coverage Rationalization and Intelligent Selection ProcedurE), a novel approach for code...
- **Link**: [Read Paper](https://doi.org/10.1145/3729401)
- **Labels**: [program testing](../../labels/program_testing.md), [general testing](../../labels/general_testing.md)


## [CXXCrafter: An LLM-Based Agent for Automated C/C++ Open Source Software Building](paper_34.md)
- **Authors**: Yu, Zhengmin and Zhang, Yuan and Wen, Ming and Nie, Yinan and Zhang, Wenhui and Yang, Min
- **Abstract**: Project building is pivotal to support various program analysis tasks, such as generating intermediate representation code for static analysis and preparing binary code for vulnerability reproduction. However, automating the building process for C/C++ projects is a highly complex endeavor, involving tremendous technical challenges, such as intricate dependency management, diverse build systems, varied toolchains, and multifaceted error handling mechanisms. Consequently, building C/C++ projects o...
- **Link**: [Read Paper](https://doi.org/10.1145/3729386)
- **Labels**: [general coding task](../../labels/general_coding_task.md), [agent design](../../labels/agent_design.md)


## [Calibration of Large Language Models on Code Summarization](paper_38.md)
- **Authors**: Virk, Yuvraj and Devanbu, Premkumar and Ahmed, Toufique
- **Abstract**: A brief, fluent, and relevant summary can be helpful during program comprehension; however, such a summary does require significant human effort to produce. Often, good summaries are unavailable in software projects, which makes maintenance more difficult. There has been a considerable body of research into automated AI-based methods, using Large Language models (LLMs), to generate summaries of code; there also has been quite a bit of work on ways to measure the performance of such summarization...
- **Link**: [Read Paper](https://doi.org/10.1145/3729400)
- **Labels**: [static analysis](../../labels/static_analysis.md), [code summarization](../../labels/code_summarization.md)


## [ChatDBG: Augmenting Debugging with Large Language Models](paper_24.md)
- **Authors**: Levin, Kyla H. and van Kempen, Nicolas and Berger, Emery D. and Freund, Stephen N.
- **Abstract**: Debugging is a critical but challenging task for programmers. This paper proposes ChatDBG, an AI-powered debugging assistant. ChatDBG integrates large language models (LLMs) to significantly enhance the capabilities and user-friendliness of conventional debuggers. ChatDBG lets programmers engage in a collaborative dialogue with the debugger, allowing them to pose complex questions about program state, perform root cause analysis for crashes or assertion failures, and explore open-ended queries l...
- **Link**: [Read Paper](https://doi.org/10.1145/3729355)
- **Labels**: [program testing](../../labels/program_testing.md), [debugging](../../labels/debugging.md)


## [Code Change Intention, Development Artifact, and History Vulnerability: Putting Them Together for Vulnerability Fix Detection by LLM](paper_8.md)
- **Authors**: Yang, Xu and Zhu, Wenhan and Pacheco, Michael and Zhou, Jiayuan and Wang, Shaowei and Hu, Xing and Liu, Kui
- **Abstract**: Detecting vulnerability fix commits in open-source software is crucial for maintaining software security. To help OSS identify vulnerability fix commits, several automated approaches are developed. However, existing approaches like VulFixMiner and CoLeFunDa, focus solely on code changes, neglecting essential context from development artifacts. Tools like Vulcurator, which integrates issue reports, fail to leverage semantic associations between different development artifacts (e.g., pull requests...
- **Link**: [Read Paper](https://doi.org/10.1145/3715738)
- **Labels**: [code generation](../../labels/code_generation.md), [program repair](../../labels/program_repair.md)


## [Code Red! On the Harmfulness of Applying Off-the-Shelf Large Language Models to Programming Tasks](paper_32.md)
- **Authors**: Al-Kaswan, Ali and Deatc, Sebastian and Ko\c{c}, Beg\"{u}m and van Deursen, Arie and Izadi, Maliheh
- **Abstract**: Nowadays, developers increasingly rely on solutions powered by Large Language Models (LLM) to assist them with their coding tasks. This makes it crucial to align these tools with human values to prevent malicious misuse.   In this paper,   we propose a comprehensive framework   for assessing the potential harmfulness   of LLMs within the software engineering domain.   We begin by developing a taxonomy of potentially harmful software engineering scenarios  and subsequently, create a dataset of pr...
- **Link**: [Read Paper](https://doi.org/10.1145/3729380)
- **Labels**: [code model](../../labels/code_model.md), [code model security](../../labels/code_model_security.md), [empirical study](../../labels/empirical_study.md)


## [CoverUp: Effective High Coverage Test Generation for Python](paper_36.md)
- **Authors**: Altmayer Pizzorno, Juan and Berger, Emery D.
- **Abstract**: Testing is an essential part of software development. Test generation tools attempt to automate the otherwise labor-intensive task of test creation, but generating high-coverage tests remains challenging. This paper proposes CoverUp, a novel approach to driving the generation of high-coverage Python regression tests. CoverUp combines coverage analysis, code context, and feedback in prompts that iteratively guide the LLM to generate tests that improve line and branch coverage.   We evaluate our p...
- **Link**: [Read Paper](https://doi.org/10.1145/3729398)
- **Labels**: [program testing](../../labels/program_testing.md), [general testing](../../labels/general_testing.md)


## [DeclarUI: Bridging Design and Development with Automated Declarative UI Code Generation](paper_6.md)
- **Authors**: Zhou, Ting and Zhao, Yanjie and Hou, Xinyi and Sun, Xiaoyu and Chen, Kai and Wang, Haoyu
- **Abstract**: Declarative UI frameworks have gained widespread adoption in mobile app development, offering benefits such as improved code readability and easier maintenance. Despite these advantages, the process of translating UI designs into functional code remains challenging and time-consuming. Recent advancements in multimodal large language models (MLLMs) have shown promise in directly generating mobile app code from user interface (UI) designs. However, the direct application of MLLMs to this task is l...
- **Link**: [Read Paper](https://doi.org/10.1145/3715726)
- **Labels**: [code generation](../../labels/code_generation.md), [program synthesis](../../labels/program_synthesis.md)


## [Demystifying Memorization in LLM-Based Program Repair via a General Hypothesis Testing Framework](paper_35.md)
- **Authors**: Kong, Jiaolong and Xie, Xiaofei and Liu, Shangqing
- **Abstract**: Large Language Models (LLMs) have achieved remarkable success in various applications, particularly in code-related tasks such as code generation and program repair, setting new performance benchmarks. However, the extensive use of large training corpora raises concerns about whether these achievements stem from genuine understanding or mere memorization of training data—a question often overlooked in current research. This paper aims to study the memorization issue within LLM-based program repa...
- **Link**: [Read Paper](https://doi.org/10.1145/3729390)
- **Labels**: [code generation](../../labels/code_generation.md), [program repair](../../labels/program_repair.md), [empirical study](../../labels/empirical_study.md)


## [Detecting and Reducing the Factual Hallucinations of Large Language Models with Metamorphic Testing](paper_20.md)
- **Authors**: Wu, Weibin and Cao, Yuhang and Yi, Ning and Ou, Rongyi and Zheng, Zibin
- **Abstract**: Question answering (QA) is a fundamental task of large language models (LLMs), which requires LLMs to automatically answer human-posed questions in natural language. However, LLMs are known to distort facts and make non-factual statements (i.e., hallucinations) when dealing with QA tasks, which may affect the deployment of LLMs in real-life situations. In this work, we propose DrHall, a framework for detecting and reducing the factual hallucinations of black-box LLMs with metamorphic testing (MT...
- **Link**: [Read Paper](https://doi.org/10.1145/3715784)
- **Labels**: [hallucination in reasoning](../../labels/hallucination_in_reasoning.md)


## [DiSCo: Towards Decompiling EVM Bytecode to Source Code using Large Language Models](paper_31.md)
- **Authors**: Su, Xing and Liang, Hanzhong and Wu, Hao and Niu, Ben and Xu, Fengyuan and Zhong, Sheng
- **Abstract**: Understanding the Ethereum smart contract bytecode is essential for ensuring cryptoeconomics security. However, existing decompilers primarily convert bytecode into pseudocode, which is not easily comprehensible for general users, potentially leading to misunderstanding of contract behavior and increased vulnerability to scams or exploits. In this paper, we propose DiSCo, the first LLMs-based EVM decompilation pipeline, which aims to enable LLMs to understand the opaque bytecode and lift it into...
- **Link**: [Read Paper](https://doi.org/10.1145/3729373)
- **Labels**: [code generation](../../labels/code_generation.md), [program decompilation](../../labels/program_decompilation.md)


## [Divide-and-Conquer: Generating UI Code from Screenshots](paper_28.md)
- **Authors**: Wan, Yuxuan and Wang, Chaozheng and Dong, Yi and Wang, Wenxuan and Li, Shuqing and Huo, Yintong and Lyu, Michael
- **Abstract**: Websites are critical in today’s digital world, with over 1.11 billion currently active and approximately 252,000 new sites launched daily. Converting website layout design into functional UI code is a time-consuming yet indispensable step of website development. Manual methods of converting visual designs into functional code present significant challenges, especially for non-experts. To explore automatic design-to-code solutions, we first conduct a motivating study on GPT-4o and identify three...
- **Link**: [Read Paper](https://doi.org/10.1145/3729364)
- **Labels**: [code generation](../../labels/code_generation.md), [program synthesis](../../labels/program_synthesis.md)


## [Doc2OracLL: Investigating the Impact of Documentation on LLM-Based Test Oracle Generation](paper_23.md)
- **Authors**: Hossain, Soneya Binta and Taylor, Raygan and Dwyer, Matthew
- **Abstract**: Code documentation is a critical artifact of software development, bridging human understanding and machine-   readable code. Beyond aiding developers in code comprehension and maintenance, documentation also plays   a critical role in automating various software engineering tasks, such as test oracle generation (TOG). In Java,   Javadoc comments offer structured, natural language documentation embedded directly within the source   code, typically describing functionality, usage, parameters, ret...
- **Link**: [Read Paper](https://doi.org/10.1145/3729354)
- **Labels**: [program testing](../../labels/program_testing.md), [general testing](../../labels/general_testing.md), [empirical study](../../labels/empirical_study.md)


## [Element-Based Automated DNN Repair with Fine-Tuned Masked Language Model](paper_3.md)
- **Authors**: Wang, Xu and Zhang, Mingming and Meng, Xiangxin and Zhang, Jian and Liu, Yang and Hu, Chunming
- **Abstract**: Deep Neural Networks (DNNs) are prevalent across a wide range of applications. Despite their success, the complexity and opaque nature of DNNs pose significant challenges in debugging and repairing DNN models, limiting their reliability and broader adoption. In this paper, we propose MLM4DNN, an element-based automated DNN repair method. Unlike previous techniques that focus on post-training adjustments or rely heavily on predefined bug patterns, MLM4DNN repairs DNNs by leveraging a fine-tuned M...
- **Link**: [Read Paper](https://doi.org/10.1145/3715716)
- **Labels**: [code generation](../../labels/code_generation.md), [program repair](../../labels/program_repair.md)


## [Eliminating Backdoors in Neural Code Models for Secure Code Understanding](paper_19.md)
- **Authors**: Sun, Weisong and Chen, Yuchen and Fang, Chunrong and Feng, Yebo and Xiao, Yuan and Guo, An and Zhang, Quanjun and Chen, Zhenyu and Xu, Baowen and Liu, Yang
- **Abstract**: Neural code models (NCMs) have been widely used to address various code understanding tasks, such as defect detection. However, numerous recent studies reveal that such models are vulnerable to backdoor attacks. Backdoored NCMs function normally on normal/clean code snippets, but exhibit adversary-expected behavior on poisoned code snippets injected with the adversary-crafted trigger. It poses a significant security threat. For example, a backdoored defect detection model may misclassify user-su...
- **Link**: [Read Paper](https://doi.org/10.1145/3715782)
- **Labels**: [code model](../../labels/code_model.md), [code model security](../../labels/code_model_security.md)


## [Error Delayed Is Not Error Handled: Understanding and Fixing Propagated Error-Handling Bugs](paper_33.md)
- **Authors**: Liu, Haoran and Li, Shanshan and Jia, Zhouyang and Zhang, Yuanliang and Bai, Linxiao and Zheng, Si and Mao, Xiaoguang and Liao, Xiangke
- **Abstract**: Error handling is critical for software reliability. In software systems, error handling may be delayed to other functions. Such propagated error handling (PEH) could easily be missed and lead to bugs. Our research reveals that PEH bugs are prevalent in software systems and, on average, take 44.1 days to fully address. Existing approaches have primarily focused on the error-handling bug within individual functions, which makes it difficult to fully address PEH bugs. In this paper, we conducted t...
- **Link**: [Read Paper](https://doi.org/10.1145/3729384)
- **Labels**: [code generation](../../labels/code_generation.md), [program repair](../../labels/program_repair.md), [static analysis](../../labels/static_analysis.md), [bug detection](../../labels/bug_detection.md)


## [Has My Code Been Stolen for Model Training? A Naturalness Based Approach to Code Contamination Detection](paper_16.md)
- **Authors**: Khan, Haris Ali and Jiang, Yanjie and Umer, Qasim and Zhang, Yuxia and Akram, Waseem and Liu, Hui
- **Abstract**: It is often valuable to know whether a given piece of source code has or hasn’t been used to train a given deep learning model. On one side, it helps avoid data contamination problems that may exaggerate the performance of evaluated models. Conversely, it facilitates copyright protection by identifying private or protected code leveraged for model training without permission. To this end, automated approaches have been proposed for the detection, known as data contamination detection. Such appro...
- **Link**: [Read Paper](https://doi.org/10.1145/3715765)
- **Labels**: [code model](../../labels/code_model.md), [code model security](../../labels/code_model_security.md)


## [Integrating Large Language Models and Reinforcement Learning for Non-linear Reasoning](paper_13.md)
- **Authors**: Alon, Yoav and David, Cristina
- **Abstract**: Large Language Models (LLMs) were shown to struggle with long-term planning, which may be caused by the limited way in which they explore the space of possible solutions. We propose an architecture where a Reinforcement Learning (RL) Agent guides an LLM's space exploration: (1) the Agent has access to domain-specific information, and can therefore make decisions about the quality of candidate solutions based on specific and relevant metrics, which were not explicitly considered by the LLM's trai...
- **Link**: [Read Paper](https://doi.org/10.1145/3715761)
- **Labels**: [agent design](../../labels/agent_design.md), [planning](../../labels/planning.md), [hallucination in reasoning](../../labels/hallucination_in_reasoning.md)


## [LLM-Based Method Name Suggestion with Automatically Generated Context-Rich Prompts](paper_11.md)
- **Authors**: Akram, Waseem and Jiang, Yanjie and Zhang, Yuxia and Khan, Haris Ali and Liu, Hui
- **Abstract**: Accurate method naming is crucial for code readability and maintainability. However, manually creating concise and meaningful names remains a significant challenge. To this end, in this paper, we propose an approach based on Large Language Model (LLMs) to suggest method names according to function descriptions. The key of the approach is ContextCraft, an automated algorithm for generating context-rich prompts for LLM that suggests the expected method names according to the prompts. For a given q...
- **Link**: [Read Paper](https://doi.org/10.1145/3715753)
- **Labels**: [code generation](../../labels/code_generation.md), [code completion](../../labels/code_completion.md)


## [LLMDroid: Enhancing Automated Mobile App GUI Testing Coverage with Large Language Model Guidance](paper_14.md)
- **Authors**: Wang, Chenxu and Liu, Tianming and Zhao, Yanjie and Yang, Minghui and Wang, Haoyu
- **Abstract**: With the rapid development of Large Language Models (LLMs), their integration into automated mobile GUI testing has emerged as a promising research direction. However, existing LLM-based testing approaches face significant challenges, including time inefficiency and high costs due to constant LLM querying. To address these issues, this paper introduces LLMDroid, a novel testing framework designed to enhance existing automated mobile GUI testing tools by leveraging LLMs more efficiently. The work...
- **Link**: [Read Paper](https://doi.org/10.1145/3715763)
- **Labels**: [program testing](../../labels/program_testing.md), [GUI testing](../../labels/GUI_testing.md)


## [Large Language Models for In-File Vulnerability Localization Can Be “Lost in the End”](paper_12.md)
- **Authors**: Sovrano, Francesco and Bauer, Adam and Bacchelli, Alberto
- **Abstract**: Traditionally, software vulnerability detection research has focused on individual small functions due to earlier language processing technologies’ limitations in handling larger inputs. However, this function-level approach may miss bugs that span multiple functions and code blocks. Recent advancements in artificial intelligence have enabled processing of larger inputs, leading everyday software developers to increasingly rely on chat-based large language models (LLMs) like GPT-3.5 and GPT-4 to...
- **Link**: [Read Paper](https://doi.org/10.1145/3715758)
- **Labels**: [static analysis](../../labels/static_analysis.md), [bug detection](../../labels/bug_detection.md), [empirical study](../../labels/empirical_study.md)


## [Less Is More: On the Importance of Data Quality for Unit Test Generation](paper_18.md)
- **Authors**: Zhang, Junwei and Hu, Xing and Gao, Shan and Xia, Xin and Lo, David and Li, Shanping
- **Abstract**: Unit testing is crucial for software development and maintenance. Effective unit testing ensures and improves software quality, but writing unit tests is time-consuming and labor-intensive. Recent studies have proposed deep learning (DL) techniques or large language models (LLMs) to automate unit test generation. These models are usually trained or fine-tuned on large-scale datasets. Despite growing awareness of the importance of data quality, there has been limited research on the quality of da...
- **Link**: [Read Paper](https://doi.org/10.1145/3715778)
- **Labels**: [program testing](../../labels/program_testing.md), [unit testing](../../labels/unit_testing.md), [empirical study](../../labels/empirical_study.md)


## [LlamaRestTest: Effective REST API Testing with Small Language Models](paper_7.md)
- **Authors**: Kim, Myeongsoo and Sinha, Saurabh and Orso, Alessandro
- **Abstract**: Modern web services rely heavily on REST APIs, typically documented using the OpenAPI specification. The widespread adoption of this standard has resulted in the development of many black-box testing tools that generate tests based on OpenAPI specifications. Although Large Language Models (LLMs) have shown promising test-generation abilities, their application to REST API testing remains mostly unexplored. We present LlamaRestTest, a novel approach that employs two custom LLMs-created by fine-tu...
- **Link**: [Read Paper](https://doi.org/10.1145/3715737)
- **Labels**: [program testing](../../labels/program_testing.md), [library testing](../../labels/library_testing.md)


## [Mystique: Automated Vulnerability Patch Porting with Semantic and Syntactic-Enhanced LLM](paper_4.md)
- **Authors**: Wu, Susheng and Wang, Ruisi and Cao, Yiheng and Chen, Bihuan and Zhou, Zhuotong and Huang, Yiheng and Zhao, JunPeng and Peng, Xin
- **Abstract**: Branching repositories facilitates efficient software development but can also inadvertently propagate vulnerabilities. When an original branch is patched, other unfixed branches remain vulnerable unless the patch is successfully ported. However, due to inherent discrepancies between branches, many patches cannot be directly applied and require manual intervention, which is time-consuming and leads to delays in patch porting, increasing vulnerability risks. Existing automated patch porting appro...
- **Link**: [Read Paper](https://doi.org/10.1145/3715718)
- **Labels**: [code generation](../../labels/code_generation.md), [program repair](../../labels/program_repair.md)


## [ReproCopilot: LLM-Driven Failure Reproduction with Dynamic Refinement](paper_37.md)
- **Authors**: Leesatapornwongsa, Tanakorn and Faisal, Fazle and Nath, Suman
- **Abstract**: Failure reproduction is a crucial step for debugging software systems, but it is often challenging and time-consuming, especially when the failures are caused by complex inputs, states, or environments. In this paper, we present ReproCopilot, a tool that leverages program analysis and a large language model (LLM) to generate a workload (i.e., code and inputs) that can reproduce a given failure. ReproCopilot proposes two novel techniques: state-oriented code generation and dynamic refinement. The...
- **Link**: [Read Paper](https://doi.org/10.1145/3729399)
- **Labels**: [program testing](../../labels/program_testing.md), [bug reproduction](../../labels/bug_reproduction.md)


## [Scientific Open-Source Software Is Less Likely to Become Abandoned Than One Might Think! Lessons from Curating a Catalog of Maintained Scientific Software](paper_30.md)
- **Authors**: Thakur, Addi Malviya and Milewicz, Reed and Jahanshahi, Mahmoud and Paganini, Lav\'{\i}nia and Vasilescu, Bogdan and Mockus, Audris
- **Abstract**: Scientific software is essential to scientific innovation and in many ways it is distinct from other types of software. Abandoned (or unmaintained), buggy, and hard to use software, a perception often associated with scientific software can hinder scientific progress, yet, in contrast to other types of software, its longevity is poorly understood. Existing data curation efforts are fragmented by science domain and/or are small in scale and lack key attributes. We use large language models to cla...
- **Link**: [Read Paper](https://doi.org/10.1145/3729369)
- **Labels**: [software maintenance and deployment](../../labels/software_maintenance_and_deployment.md), [empirical study](../../labels/empirical_study.md)


## [Smaller but Better: Self-Paced Knowledge Distillation for Lightweight yet Effective LCMs](paper_42.md)
- **Authors**: Chen, Yujia and Ye, Yang and Li, Zhongqi and Ma, Yuchi and Gao, Cuiyun
- **Abstract**: Large code models (LCMs) have remarkably advanced the field of code generation. Despite their impressive capabilities, they still face practical deployment issues, such as high inference costs, limited accessibility of proprietary LCMs, and adaptability issues of ultra-large LCMs. These issues highlight the critical need for more accessible, lightweight yet effective LCMs. Knowledge distillation (KD) offers a promising solution, which transfers the programming capabilities of larger, advanced LC...
- **Link**: [Read Paper](https://doi.org/10.1145/3729405)
- **Labels**: [code generation](../../labels/code_generation.md), [program synthesis](../../labels/program_synthesis.md), [code model](../../labels/code_model.md), [code model training](../../labels/code_model_training.md)


## [SmartNote: An LLM-Powered, Personalised Release Note Generator That Just Works](paper_22.md)
- **Authors**: Daneshyan, Farbod and He, Runzhi and Wu, Jianyu and Zhou, Minghui
- **Abstract**: The release note is a crucial document outlining changes in new software versions. It plays a key role in helping stakeholders recognise important changes and understand the implications behind them. Despite this fact, many developers view the process of writing software release notes as a tedious and dreadful task. Consequently, numerous tools (e.g., DeepRelease and Conventional Changelog) have been developed by researchers and practitioners to automate the generation of software release notes....
- **Link**: [Read Paper](https://doi.org/10.1145/3729345)
- **Labels**: [documentation generation](../../labels/documentation_generation.md), [software maintenance and deployment](../../labels/software_maintenance_and_deployment.md)


## [Statement-Level Adversarial Attack on Vulnerability Detection Models via Out-of-Distribution Features](paper_41.md)
- **Authors**: Du, Xiaohu and Wen, Ming and Wang, Haoyu and Wei, Zichao and Jin, Hai
- **Abstract**: Code vulnerability detection is crucial to ensure software security. Recent advancements, particularly with the emergence of Code Pre-Trained Models (CodePTMs) and Large Language Models (LLMs), have led to significant progress in this area. However, these models are easily susceptible to adversarial attacks, where even slight input modifications can lead the models to generate opposite results. Existing adversarial approaches, such as identifier replacement, code transformation, and dead code in...
- **Link**: [Read Paper](https://doi.org/10.1145/3729403)
- **Labels**: [code model](../../labels/code_model.md), [code model robustness](../../labels/code_model_robustness.md), [static analysis](../../labels/static_analysis.md), [bug detection](../../labels/bug_detection.md)


## [The Struggles of LLMs in Cross-Lingual Code Clone Detection](paper_15.md)
- **Authors**: Moumoula, Micheline B\'{e}n\'{e}dicte and Kabor\'{e}, Abdoul Kader and Klein, Jacques and Bissyand\'{e}, Tegawend\'{e} F.
- **Abstract**: With the involvement of multiple programming languages in modern software development, cross-lingual code clone detection has gained traction within the software engineering community. Numerous studies have explored this topic, proposing various promising approaches. Inspired by the significant advances in machine learning in recent years, particularly Large Language Models (LLMs), which have demonstrated their ability to tackle various tasks, this paper revisits cross-lingual code clone detecti...
- **Link**: [Read Paper](https://doi.org/10.1145/3715764)
- **Labels**: [empirical study](../../labels/empirical_study.md), [static analysis](../../labels/static_analysis.md), [code similarity analysis](../../labels/code_similarity_analysis.md)


## [Zero-Shot Cross-Domain Code Search without Fine-Tuning](paper_26.md)
- **Authors**: Liang, Keyu and Liu, Zhongxin and Liu, Chao and Wan, Zhiyuan and Lo, David and Yang, Xiaohu
- **Abstract**: Code search is a crucial task in software engineering, aiming to retrieve code snippets that are semantically relevant to a natural language query. Recently, Pre-trained Language Models (PLMs) have shown remarkable success and are widely adopted for code search tasks. However, PLM-based methods often struggle in cross-domain scenarios. When applied to a new domain, they typically require extensive fine-tuning with substantial data. Even worse, the data scarcity problem in new domains often force...
- **Link**: [Read Paper](https://doi.org/10.1145/3729357)
- **Labels**: [static analysis](../../labels/static_analysis.md), [code search](../../labels/code_search.md)
