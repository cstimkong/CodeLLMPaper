# Enhancing Vulnerability Detection via Inter-procedural Semantic Completion

**Authors**: Wu, Bozhi and Liu, Chengjie and Li, Zhiming and Cao, Yushi and Sun, Jun and Lin, Shang-Wei

**Abstract**:

Inspired by advances in deep learning, numerous learning-based approaches for vulnerability detection have emerged, primarily operating at the function level for scalability. However, this design choice has a critical limitation: many vulnerabilities span multiple functions, causing function-level approaches to lose the semantics of called functions and fail to capture true vulnerability patterns. To address this issue, we propose VulnSC, a novel framework designed to enhance learning-based approaches by complementing inter-procedural semantics. VulnSC retrieves the source code of called functions for datasets and leverages large language models (LLMs) with well-designed prompts to generate summaries for these functions. The datasets, enhanced with these summaries, are fed into neural networks for improved vulnerability detection. VulnSC is the first general framework to integrate inter-procedural semantics into existing learning-based approaches for vulnerability detection while maintaining scalability. We evaluate VulnSC on four state-of-the-art learning-based approaches using two widely used datasets, and our experimental results demonstrate that VulnSC significantly enhances detection performance with minimal additional computational overhead.

**Link**: [Read Paper](https://doi.org/10.1145/3728912)

**Labels**: [static analysis](../../labels/static_analysis.md), [bug detection](../../labels/bug_detection.md), [code summarization](../../labels/code_summarization.md)
