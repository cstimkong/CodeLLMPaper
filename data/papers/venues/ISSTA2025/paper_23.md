# OpDiffer: LLM-Assisted Opcode-Level Differential Testing of Ethereum Virtual Machine

**Authors**: Ma, Jie and He, Ningyu and Xi, Jinwen and Xing, Mingzhe and Wang, Haoyu and Gao, Ying and Yue, Yinliang

**Abstract**:

As Ethereum continues to thrive, the Ethereum Virtual Machine (EVM) has become the cornerstone powering tens of millions of active smart contracts. Intuitively, security issues in EVMs could lead to inconsistent behaviors among smart contracts or even denial-of-service of the entire blockchain network. However, to the best of our knowledge, only a limited number of studies focus on the security of EVMs. Moreover, they suffer from 1) insufficient test input diversity and invalid semantics; and 2) the inability to automatically identify bugs and locate root causes.   To bridge this gap, we propose OpDiffer, a differential testing framework for EVM, which takes advantage of LLMs and static analysis methods to address the above two limitations.   We conducted the largest-scale evaluation, covering nine EVMs and uncovering 26 previously unknown bugs, 22 of which have been confirmed by developers and three have been assigned CNVD IDs. Compared to state-of-the-art baselines, OpDiffer can improve code coverage by at most 71.06\%, 148.40\% and 655.56\%, respectively. Through an analysis of real-world deployed Ethereum contracts, we estimate that 7.21\% of the contracts could trigger our identified EVM bugs under certain environmental settings, potentially resulting in severe negative impact on the Ethereum ecosystem.

**Link**: [Read Paper](https://doi.org/10.1145/3728946)

**Labels**: [program testing](../../labels/program_testing.md), [differential testing](../../labels/differential_testing.md)
