# Error Delayed Is Not Error Handled: Understanding and Fixing Propagated Error-Handling Bugs

**Authors**: Liu, Haoran and Li, Shanshan and Jia, Zhouyang and Zhang, Yuanliang and Bai, Linxiao and Zheng, Si and Mao, Xiaoguang and Liao, Xiangke

**Abstract**:

Error handling is critical for software reliability. In software systems, error handling may be delayed to other functions. Such propagated error handling (PEH) could easily be missed and lead to bugs. Our research reveals that PEH bugs are prevalent in software systems and, on average, take 44.1 days to fully address. Existing approaches have primarily focused on the error-handling bug within individual functions, which makes it difficult to fully address PEH bugs. In this paper, we conducted the first in-depth study on PEH bugs in 11 mature software systems, examining how errors propagate and how they should be handled. We introduce EH-Fixer, an LLM-based tool for automated program repair specifically designed to address PEH bugs. For each PEH bug, EH-Fixer constructs its propagation path, and repairs them through retrieval-augmented generation. To assess the performance of our approach, we collected 89 historical PEH bugs from the Linux Kernel as well as 9 widely used applications. The experimental results show that EH-Fixer can fix 83.1\% (74/89) of PEH bugs.

**Link**: [Read Paper](https://doi.org/10.1145/3729384)

**Labels**: [code generation](../../labels/code_generation.md), [program repair](../../labels/program_repair.md), [static analysis](../../labels/static_analysis.md), [bug detection](../../labels/bug_detection.md)
