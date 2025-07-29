# VerLog: Enhancing Release Note Generation for Android Apps using Large Language Models

**Authors**: Guo, Jiawei and Yang, Haoran and Cai, Haipeng

**Abstract**:

Release notes are essential documents that communicate the details of software updates to users and developers, yet their generation remains a time-consuming and error-prone process. In this paper, we present VerLog, a novel technique that enhances the generation of software release notes using Large Language Models (LLMs). VerLog leverages few-shot in-context learning with adaptive prompting to facilitate the graph reasoning capabilities of LLMs, enabling them to accurately interpret and document the semantic information of code changes. Additionally, VerLog incorporates multi-granularity information, including fine-grained code modifications and high-level non-code artifacts, to guide the generation process and ensure comprehensive, accurate, and readable release notes. We applied VerLog to the 42 releases of 248 unique Android applications and conducted extensive evaluations. Our results demonstrate that VerLog significantly (up to 18\%–21\% higher precision, recall, and F1) outperforms state-of-the-art baselines in terms of completeness, accuracy, readability, and overall quality of the generated release notes, in both controlled experiments with high-quality reference release notes and in-the-wild evaluations.

**Link**: [Read Paper](https://doi.org/10.1145/3728961)

**Labels**: [software maintenance and deployment](../../labels/software_maintenance_and_deployment.md), [documentation generation](../../labels/documentation_generation.md)
