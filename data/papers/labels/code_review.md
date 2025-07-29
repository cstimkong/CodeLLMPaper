# Code Review

- [An Empirical Study on Code Review Activity Prediction and Its Impact in Practice](../venues/FSE2024/paper_10.md), ([FSE2024](../venues/FSE2024/README.md))

  - **Abstract**: During code reviews, an essential step in software quality assurance, reviewers have the difficult task of understanding and evaluating code changes to validate their quality and prevent introducing faults to the codebase. This is a tedious process where the effort needed is highly dependent on the code submitted, as well as the author’s and the reviewer’s experience, leading to median wait times for review feedback of 15-64 hours. Through an initial user study carried with 29 experts, we found ...
  - **Labels**: [software maintenance and deployment](software_maintenance_and_deployment.md), [code review](code_review.md), [empirical study](empirical_study.md)


- [Can LLMs Replace Human Evaluators? An Empirical Study of LLM-as-a-Judge in Software Engineering](../venues/ISSTA2025/paper_30.md), ([ISSTA2025](../venues/ISSTA2025/README.md))

  - **Abstract**: Recently, large language models (LLMs) have been deployed to tackle various software engineering (SE) tasks like code generation, significantly advancing the automation of SE tasks. However, assessing the quality of these LLM-generated code and text remains challenging. The commonly used Pass@k metric necessitates extensive unit tests and configured environments, demands a high labor cost, and is not suitable for evaluating LLM-generated text. Conventional metrics like BLEU, which measure only l...
  - **Labels**: [software maintenance and deployment](software_maintenance_and_deployment.md), [code review](code_review.md), [empirical study](empirical_study.md)


- [Code Review Automation: Strengths and Weaknesses of the State of the Art](../venues/TSE2024/paper_9.md), ([TSE2024](../venues/TSE2024/README.md))

  - **Abstract**: The automation of code review has been tackled by several researchers with the goal of reducing its cost. The adoption of deep learning in software engineering pushed the automation to new boundaries, with techniques &lt;italic&gt;imitating&lt;/italic&gt; developers in generative tasks, such as commenting on a code change as a reviewer would do or addressing a reviewer's comment by modifying code. The performance of these techniques is usually assessed through quantitative metrics, &lt;italic&gt...
  - **Labels**: [code review](code_review.md), [empirical study](empirical_study.md)


- [CodeAgent: Autonomous Communicative Agents for Code Review](../venues/EMNLP2024/paper_26.md), ([EMNLP2024](../venues/EMNLP2024/README.md))

  - **Abstract**: Code review, which aims at ensuring the overall quality and reliability of software, is a cornerstone of software development. Unfortunately, while crucial, Code review is a labor-intensive process that the research community is looking to automate. Existing automated methods rely on single input-output generative models and thus generally struggle to emulate the collaborative nature of code review. This work introduces CodeAgent, a novel multi-agent Large Language Model (LLM) system for code re...
  - **Labels**: [software maintenance and deployment](software_maintenance_and_deployment.md), [code review](code_review.md), [agent design](agent_design.md)


- [PatchScope: LLM-Enhanced Fine-Grained Stable Patch Classification for Linux Kernel](../venues/ISSTA2025/paper_21.md), ([ISSTA2025](../venues/ISSTA2025/README.md))

  - **Abstract**: Stable patch classification plays a crucial role in vulnerability management for the Linux kernel, significantly contributing to the stability and security of Long-term support(LTS) versions. Although existing tools have effectively assisted in assessing whether patches should be merged into stable versions, they cannot determine which stable patches should be merged into which LTS versions. This process still requires the maintainers of the distribution community to manually screen based on the...
  - **Labels**: [software maintenance and deployment](software_maintenance_and_deployment.md), [code review](code_review.md)


- [SCPatcher: Mining Crowd Security Discussions to Enrich Secure Coding Practices](../venues/ASE2023/paper_8.md), ([ASE2023](../venues/ASE2023/README.md))

  - **Abstract**: Secure coding practices (SCPs) have been proposed to guide software developers to write code securely to prevent potential security vulnerabilities. Yet, they are typically one-sentence principles without detailed specifications, e.g., “Properly free allocated memory upon the completion of functions and at all exit points.”, which makes them difficult to follow in practice, especially for software developers who are not yet experienced in secure programming. To address this problem, this paper p...
  - **Labels**: [software maintenance and deployment](software_maintenance_and_deployment.md), [code review](code_review.md)


- [Semantic GUI Scene Learning and Video Alignment for Detecting Duplicate Video-based Bug Reports](../venues/ICSE2024/paper_32.md), ([ICSE2024](../venues/ICSE2024/README.md))

  - **Abstract**: Video-based bug reports are increasingly being used to document bugs for programs centered around a graphical user interface (GUI). However, developing automated techniques to manage video-based reports is challenging as it requires identifying and understanding often nuanced visual patterns that capture key information about a reported bug. In this paper, we aim to overcome these challenges by advancing the bug report management task of duplicate detection for video-based reports. To this end, ...
  - **Labels**: [software maintenance and deployment](software_maintenance_and_deployment.md), [code review](code_review.md)


- [Understanding Developer-Analyzer Interactions in Code Reviews](../venues/ASE2024/paper_29.md), ([ASE2024](../venues/ASE2024/README.md))

  - **Abstract**: Static code analyzers are now a common part of the codereview process. These automated tools integrate into the code review process by commenting on code changes and suggesting improvements, in the same way as human reviewers. The comments made by static analyzers often trigger a conversation between developers to align on if and how the issue should be fixed. Because developers rarely give feedback directly to the tool, understanding the sentiment and intent in the conversation triggered by the...
  - **Labels**: [software maintenance and deployment](software_maintenance_and_deployment.md), [code review](code_review.md), [empirical study](empirical_study.md)


- [{CRS}core: Grounding Automated Evaluation of Code Review Comments in Code Claims and Smells](../venues/NAACL2025/paper_7.md), ([NAACL2025](../venues/NAACL2025/README.md))

  - **Abstract**: The task of automated code review has recently gained a lot of attention from the machine learning community. However, current review comment evaluation metrics rely on comparisons with a human-written reference for a given code change (also called a diff ). Furthermore, code review is a one-to-many problem, like generation and summarization, with many ``valid reviews'' for a diff. Thus, we develop CRScore {---} a reference-free metric to measure dimensions of review quality like conciseness, co...
  - **Labels**: [software maintenance and deployment](software_maintenance_and_deployment.md), [code review](code_review.md)
