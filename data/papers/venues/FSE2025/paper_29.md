# Automatically Fixing Dependency Breaking Changes

**Authors**: Fruntke, Lukas and Krinke, Jens

**Abstract**:

Breaking changes in dependencies are a common challenge in software development, requiring manual intervention to resolve. This study examines how well LLM automate the repair of breaking changes caused by dependency updates in Java projects. Although earlier methods have mostly concentrated on detecting breaking changes or investigating their impact, they have not been able to completely automate the repair process. We introduce and compare two new approaches: an agentic system that combines automated tool usage with LLM, and a recursive zero-shot approach, employing iterative prompt refinement. Our experimental framework assesses the repair success of both approaches, using the BUMP dataset of curated breaking changes. We also investigate the impact of variables such as dependency popularity and prompt configuration on repair outcomes. Our results demonstrate a substantial difference in test suite success rates, with the agentic approach achieving a repair success rate of up to 23\%, while the zero-shot prompting approach achieved a repair success rate of up to 19\%. We show that automated program repair of breaking dependencies with LLMs is feasible and can be optimised to achieve better repair outcomes.

**Link**: [Read Paper](https://doi.org/10.1145/3729366)

**Labels**: [code generation](../../labels/code_generation.md), [program repair](../../labels/program_repair.md)
