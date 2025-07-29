# OmniGIRL: A Multilingual and Multimodal Benchmark for GitHub Issue Resolution

**Authors**: Guo, Lianghong and Tao, Wei and Jiang, Runhan and Wang, Yanlin and Chen, Jiachi and Liu, Xilin and Ma, Yuchi and Mao, Mingzhi and Zhang, Hongyu and Zheng, Zibin

**Abstract**:

The GitHub issue resolution task aims to resolve issues reported in repositories automatically. With advances in large language models (LLMs), this task has gained increasing attention, and several benchmarks are proposed to evaluate the issue resolution ability of LLMs. However, existing benchmarks have three main limitations. First, current benchmarks focus on a single programming language, limiting the evaluation of issues from repositories across different languages. Second, they usually cover a narrow range of domains, which may fail to represent the diversity of real-world issues. Third, existing benchmarks rely solely on textual information in issue descriptions, overlooking multimodal information such as images in issues. In this paper, we propose OmniGIRL, a GitHub Issue ResoLution benchmark that is multilingual, multimodal, and multi-domain. OmniGIRL includes 959 task instances, which are collected from repositories across four programming languages (i.e., Python, JavaScript, TypeScript, and Java) and eight different domains. Our evaluation shows that current LLMs show limited performances on OmniGIRL. Notably, the best-performing model, GPT-4o, resolves only 8.6\% of the issues. Besides, we find that current LLMs struggle to resolve issues requiring understanding images. The best performance is achieved by Claude-3.5-Sonnet, which resolves only 10.5\% of the issues with image information. Finally, we analyze the reasons behind current LLMs’ failure on OmniGIRL, providing insights for future improvements.

**Link**: [Read Paper](https://doi.org/10.1145/3728871)

**Labels**: [code generation](../../labels/code_generation.md), [program repair](../../labels/program_repair.md)
