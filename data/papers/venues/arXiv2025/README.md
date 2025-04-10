# arXiv2025

Number of papers: 12

## [AI Software Engineer: Programming with Trust](paper_10.md)
- **Authors**: Abhik Roychoudhury, Corina Pasareanu, Michael Pradel, Baishakhi Ray
- **Abstract**: Large Language Models (LLMs) have shown surprising proficiency in generating code snippets, promising to automate large parts of software engineering via artificial intelligence (AI). We argue that successfully deploying AI software engineers requires a level of trust equal to or even greater than the trust established by human-driven software engineering practices. The recent trend toward LLM agents offers a path toward integrating the power of LLMs to create new code with the power of analysis...
- **Link**: [Read Paper](https://arxiv.org/pdf/2502.13767)
- **Labels**: [code generation](../../labels/code_generation.md), [survey](../../labels/survey.md)


## [C2SaferRust: Transforming C Projects into Safer Rust with NeuroSymbolic Techniques](paper_12.md)
- **Authors**: Vikram Nitin, Rahul Krishna, Luiz Lemos do Valle, Baishakhi Ray
- **Abstract**: In recent years, there has been a lot of interest in converting C code to Rust, to benefit from the memory and thread safety guarantees of Rust. C2Rust is a rule-based system that can automatically convert C code to functionally identical Rust, but the Rust code that it produces is non-idiomatic, i.e., makes extensive use of unsafe Rust, a subset of the language that doesn't have memory or thread safety guarantees. At the other end of the spectrum are LLMs, which produce idiomatic Rust code, but...
- **Link**: [Read Paper](https://arxiv.org/pdf/2501.14257)
- **Labels**: [code generation](../../labels/code_generation.md), [program transformation](../../labels/program_transformation.md)


## [CVE-Bench: A Benchmark for AI Agents' Ability to Exploit Real-World Web Application Vulnerabilities](paper_9.md)
- **Authors**: Yuxuan Zhu, Antony Kellermann, Dylan Bowman, Philip Li, Akul Gupta, Adarsh Danda, Richard Fang, Conner Jensen, Eric Ihli, Jason Benn, Jet Geronimo, Avi Dhir, Sudhit Rao, Kaicheng Yu, Twm Stone, Daniel Kang
- **Abstract**: Large language model (LLM) agents are increasingly capable of autonomously conducting cyberattacks, posing significant threats to existing applications. This growing risk highlights the urgent need for a real-world benchmark to evaluate the ability of LLM agents to exploit web application vulnerabilities. However, existing benchmarks fall short as they are limited to abstracted Capture the Flag competitions or lack comprehensive coverage. Building a benchmark for real-world vulnerabilities invol...
- **Link**: [Read Paper](https://arxiv.org/abs/2503.17332)
- **Labels**: [program testing](../../labels/program_testing.md), [vulnerability exploitation](../../labels/vulnerability_exploitation.md)


## [Can LLMs Reason About Program Semantics? A Comprehensive Evaluation of LLMs on Formal Specification Inference](paper_5.md)
- **Authors**: Thanh Le-Cong, Bach Le, Toby Murray
- **Abstract**: Large Language Models (LLMs) are increasingly being used to automate programming tasks. Yet, LLMs' capabilities in reasoning about program semantics are still inadequately studied, leaving significant potential for further exploration. This paper introduces FormalBench, a comprehensive benchmark designed to evaluate LLMs' reasoning abilities on program semantics, particularly via the task of synthesizing formal program specifications to assist verifying program correctness. This task requires bo...
- **Link**: [Read Paper](https://arxiv.org/abs/2503.04779)
- **Labels**: [static analysis](../../labels/static_analysis.md), [specification inference](../../labels/specification_inference.md), [benchmark](../../labels/benchmark.md), [empirical study](../../labels/empirical_study.md)


## [ClassInvGen: Class Invariant Synthesis using Large Language Models](paper_8.md)
- **Authors**: Chuyue Sun, Viraj Agashe, Saikat Chakraborty, Jubi Taneja, Clark Barrett, David Dill, Xiaokang Qiu, Shuvendu K. Lahiri
- **Abstract**: Formal program specifications in the form of preconditions, postconditions, and class invariants have several benefits for the construction and maintenance of programs. They not only aid in program understanding due to their unambiguous semantics but can also be enforced dynamically (or even statically when the language supports a formal verifier). However, synthesizing high-quality specifications in an underlying programming language is limited by the expressivity of the specifications or the n...
- **Link**: [Read Paper](https://www.arxiv.org/abs/2502.18917)
- **Labels**: [static analysis](../../labels/static_analysis.md), [program verification](../../labels/program_verification.md)


## [Combining Large Language Models with Static Analyzers for Code Review Generation](paper_7.md)
- **Authors**: Rohit Gheyi, Marcio Ribeiro, Jonhnanthan Oliveira
- **Abstract**: Code review is a crucial but often complex, subjective, and time-consuming activity in software development. Over the past decades, significant efforts have been made to automate this process. Early approaches focused on knowledge-based systems (KBS) that apply rule-based mechanisms to detect code issues, providing precise feedback but struggling with complex, context-dependent cases. More recent work has shifted toward fine-tuning pre-trained language models for code review, enabling broader is...
- **Link**: [Read Paper](https://arxiv.org/pdf/2502.06633)
- **Labels**: [static analysis](../../labels/static_analysis.md), [bug detection](../../labels/bug_detection.md)


## [Evaluating the Effectiveness of Small Language Models in Detecting Refactoring Bugs](paper_6.md)
- **Authors**: Rohit Gheyi, Marcio Ribeiro, Jonhnanthan Oliveira
- **Abstract**: Popular IDEs frequently contain bugs in their refactoring implementations. Ensuring that a transformation preserves a program's behavior is a complex task. Traditional detection methods rely on predefined preconditions for each refactoring type, limiting their scalability and adaptability to new transformations. These methods often require extensive static and dynamic analyses, which are computationally expensive, time-consuming, and may still fail to detect certain refactoring bugs. This study ...
- **Link**: [Read Paper](https://arxiv.org/abs/2502.18454)
- **Labels**: [static analysis](../../labels/static_analysis.md), [bug detection](../../labels/bug_detection.md)


## [Hierarchical Repository-Level Code Summarization for Business Applications Using Local LLMs](paper_11.md)
- **Authors**: Nilesh Dhulshette, Sapan Shah, Vinay Kulkarni
- **Abstract**: In large-scale software development, understanding the functionality and intent behind complex codebases is critical for effective development and maintenance. While code summarization has been widely studied, existing methods primarily focus on smaller code units, such as functions, and struggle with larger code artifacts like files and packages. Additionally, current summarization models tend to emphasize low-level implementation details, often overlooking the domain and business context that ...
- **Link**: [Read Paper](https://arxiv.org/pdf/2501.07857)
- **Labels**: [static analysis](../../labels/static_analysis.md), [code summarization](../../labels/code_summarization.md), [agent design](../../labels/agent_design.md), [prompt strategy](../../labels/prompt_strategy.md), [retrieval-augmented generation](../../labels/retrieval-augmented_generation.md)


## [Is Your Benchmark (Still) Useful? Dynamic Benchmarking for Code Language Models](paper_3.md)
- **Authors**: Batu Guan, Xiao Wu, Yuanyuan Yuan, Shaohua Li
- **Abstract**: In this paper, we tackle a critical challenge in model evaluation: how to keep code benchmarks useful when models might have already seen them during training. We introduce a novel solution, dynamic benchmarking framework, to address this challenge. Given a code understanding or reasoning benchmark, our framework dynamically transforms each input, i.e., programs, with various semantic-preserving mutations to build a syntactically new while semantically identical benchmark. We evaluated ten popul...
- **Link**: [Read Paper](https://arxiv.org/abs/2503.06643)
- **Labels**: [benchmark](../../labels/benchmark.md)


## [KNighter: Transforming Static Analysis with LLM-Synthesized Checkers](paper_4.md)
- **Authors**: Chenyuan Yang, Zijie Zhao, Zichen Xie, Haoyu Li, Lingming Zhang
- **Abstract**: Static analysis is a powerful technique for bug detection in critical systems like operating system kernels. However, designing and implementing static analyzers is challenging, timeconsuming, and typically limited to predefined bug patterns. While large language models (LLMs) have shown promise for static analysis, directly applying them to scan large codebases remains impractical due to computational constraints and contextual limitations. We present KNighter, the first approach that unlocks p...
- **Link**: [Read Paper](https://arxiv.org/pdf/2503.09002)
- **Labels**: [static analysis](../../labels/static_analysis.md), [bug detection](../../labels/bug_detection.md)


## [LAMD: Context-driven Android Malware Detection and Classification with LLMs](paper_1.md)
- **Authors**: Xingzhi Qian, Xinran Zheng, Yiling He, Shuo Yang, Lorenzo Cavallaro
- **Abstract**: The rapid growth of mobile applications has escalated Android malware threats. Although there are numerous detection methods, they often struggle with evolving attacks, dataset biases, and limited explainability. Large Language Models (LLMs) offer a promising alternative with their zero-shot inference and reasoning capabilities. However, applying LLMs to Android malware detection presents two key challenges: (1)the extensive support code in Android applications, often spanning thousands of class...
- **Link**: [Read Paper](https://www.arxiv.org/pdf/2502.13055)
- **Labels**: [static analysis](../../labels/static_analysis.md), [bug detection](../../labels/bug_detection.md)


## [Language Models for Code Optimization: Survey, Challenges and Future Directions](paper_2.md)
- **Authors**: Jingzhi Gong, Vardan Voskanyan, Paul Brookes, Fan Wu, Wei Jie, Jie Xu, Rafail Giavrimis, Mike Basios, Leslie Kanthan, Zheng Wang
- **Abstract**: Language models (LMs) built upon deep neural networks (DNNs) have recently demonstrated breakthrough effectiveness in software engineering tasks such as code generation, completion, and repair. This has paved the way for the emergence of LM-based code optimization techniques, which are crucial for enhancing the performance of existing programs, such as accelerating program execution time. However, a comprehensive survey dedicated to this specific application has been lacking. To fill this gap, w...
- **Link**: [Read Paper](https://arxiv.org/abs/2501.01277)
- **Labels**: [static analysis](../../labels/static_analysis.md), [program optimization](../../labels/program_optimization.md), [survey](../../labels/survey.md)
