# Identifying Multi-parameter Constraint Errors in Python Data Science Library API Documentation

**Authors**: Xu, Xiufeng and Xie, Fuman and Zhu, Chenguang and Bai, Guangdong and Khurshid, Sarfraz and Li, Yi

**Abstract**:

Modern AI- and Data-intensive software systems rely heavily on data science and machine learning libraries that provide essential algorithmic implementations and computational frameworks. These libraries expose complex APIs whose correct usage has to follow constraints among multiple interdependent parameters. Developers using these APIs are expected to learn about the constraints through the provided documentation and any discrepancy may lead to unexpected behaviors. However, maintaining correct and consistent multi-parameter constraints in API documentation remains a significant challenge for API compatibility and reliability. To address this challenge, we propose MPChecker for detecting inconsistencies between code and documentation, specifically focusing on multi-parameter constraints. MPChecker identifies these constraints at the code level by exploring execution paths through symbolic execution and further extracts corresponding constraints from documentation using large language models (LLMs). We propose a customized fuzzy constraint logic to reconcile the unpredictability of LLM outputs and detect logical inconsistencies between the code and documentation constraints. We collected and constructed two datasets from four popular data science libraries and evaluated MPChecker on them. Our tool identified 117 of 126 inconsistent constraints, achieving a recall of 92.8\% and demonstrating its effectiveness at detecting inconsistency issues. We further reported 14 detected inconsistency issues to the library developers, who have confirmed 11 issues at the time of writing.

**Link**: [Read Paper](https://doi.org/10.1145/3728945)

**Labels**: [static analysis](../../labels/static_analysis.md), [bug detection](../../labels/bug_detection.md)
