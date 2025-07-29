# REACCEPT: Automated Co-evolution of Production and Test Code Based on Dynamic Validation and Large Language Models

**Authors**: Chi, Jianlei and Wang, Xiaotian and Huang, Yuhan and Yu, Lechen and Cui, Di and Sun, Jianguo and Sun, Jun

**Abstract**:

Synchronizing production and test code, known as PT co-evolution, is critical for software quality. Given the significant manual effort involved, researchers have tried automating PT co-evolution using predefined heuristics and machine learning models. However, existing solutions are still incomplete. Most approaches only detect and flag obsolete test cases, leaving developers to manually update them. Meanwhile, existing solutions may suffer from low accuracy, especially when applied to real-world software projects.   In this paper, we propose ReAccept, a novel approach leveraging large language models (LLMs), retrievalaugmented generation (RAG), and dynamic validation to fully automate PT co-evolution with high accuracy. ReAccept employs an experience-guided approach to generate prompt templates for the identification and subsequent update processes. After updating a test case, ReAccept performs dynamic validation by checking syntax, verifying semantics, and assessing test coverage. If the validation fails, ReAccept leverages the error messages to iteratively refine the patch. To evaluate ReAccept's effectiveness, we conducted extensive experiments with a dataset of 537 Java projects and compared ReAccept's performance with several stateof-the-art methods. The evaluation results show that ReAccept achieved an update accuracy of 60.16\% on the correctly identified obsolete test code, surpassing the state-of-the-art technique CEPROT by 90\%. These findings demonstrate that ReAccept can effectively maintain test code, improve overall software quality, and significantly reduce maintenance effort.

**Link**: [Read Paper](https://doi.org/10.1145/3728930)

**Labels**: [program testing](../../labels/program_testing.md), [code generation](../../labels/code_generation.md)
