# ReproCopilot: LLM-Driven Failure Reproduction with Dynamic Refinement

**Authors**: Leesatapornwongsa, Tanakorn and Faisal, Fazle and Nath, Suman

**Abstract**:

Failure reproduction is a crucial step for debugging software systems, but it is often challenging and time-consuming, especially when the failures are caused by complex inputs, states, or environments. In this paper, we present ReproCopilot, a tool that leverages program analysis and a large language model (LLM) to generate a workload (i.e., code and inputs) that can reproduce a given failure. ReproCopilot proposes two novel techniques: state-oriented code generation and dynamic refinement. These techniques can iteratively guide the LLM with program analysis feedback until the generated workload can successfully reproduce the target failure. We evaluate ReproCopilot on 50 real-world failures from 17 open-source projects, and show that it can reproduce 76\% of them, significantly outperforming the-state-of-the-art solutions.

**Link**: [Read Paper](https://doi.org/10.1145/3729399)

**Labels**: [program testing](../../labels/program_testing.md), [bug reproduction](../../labels/bug_reproduction.md)
