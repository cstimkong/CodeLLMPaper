# Automatically Inspecting Thousands of Static Bug Warnings with Large Language Model: How Far Are We?

**Authors**: Cheng Wen, Yuandao Cai, Bin Zhang, Jie Su, Zhiwu Xu, Dugang Liu, Shengchao Qin, Zhong Ming, Tian Cong

**Abstract**:

Static analysis tools for capturing bugs and vulnerabilities in software programs are widely employed in practice, as they have the unique advantages of high coverage and independence from the execution environment. However, existing tools for analyzing large codebases often produce a great deal of false warnings over genuine bug reports. As a result, developers are required to manually inspect and confirm each warning, a challenging, time-consuming, and automation-essential task.
 This article advocates a fast, general, and easily extensible approach called Llm4sa that automatically inspects a sheer volume of static warnings by harnessing (some of) the powers of Large Language Models (LLMs). Our key insight is that LLMs have advanced program understanding capabilities, enabling them to effectively act as human experts in conducting manual inspections on bug warnings with their relevant code snippets. In this spirit, we propose a static analysis to effectively extract the relevant code snippets via program dependence traversal guided by the bug warning reports themselves. Then, by formulating customized questions that are enriched with domain knowledge and representative cases to query LLMs, Llm4sa can remove a great deal of false warnings and facilitate bug discovery significantly. Our experiments demonstrate that Llm4sa is practical in automatically inspecting thousands of static warnings from Juliet benchmark programs and 11 real-world C/C++ projects, showcasing a high precision (81.13%) and a recall rate (94.64%) for a total of 9,547 bug warnings. Our research introduces new opportunities and methodologies for using the LLMs to reduce human labor costs, improve the precision of static analyzers, and ensure software trustworthiness

**Link**: [Read Paper](https://dl.acm.org/doi/pdf/10.1145/3653718)

**Labels**: [static analysis](../../labels/static_analysis.md), [bug detection](../../labels/bug_detection.md)
