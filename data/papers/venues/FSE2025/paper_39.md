# CRISPE: Semantic-Guided Execution Planning and Dynamic Reasoning for Enhancing Code Coverage Prediction

**Authors**: Dhulipala, Hridya and Yadavally, Aashish and Patel, Smit Soneshbhai and Nguyen, Tien N.

**Abstract**:

While LLMs excel in understanding source code and descriptive texts for tasks like code generation, code completion, etc., they exhibit weaknesses in predicting dynamic program behavior, such as code coverage and runtime error detection, which typically require program execution. Aiming to advance the capability of LLMs in reasoning and predicting the program behavior at runtime, we present CRISPE (short for Coverage Rationalization and Intelligent Selection ProcedurE), a novel approach for code coverage prediction. CRISPE guides an LLM in simulating program execution via an execution plan based on two key factors: (1) program semantics of each statement type, and (2) the observation of the set of covered statements at the current “execution” step relative to all feasible code coverage options. We formulate code coverage prediction as a process of semantic-guided execution-based planning, where feasible coverage options are utilized to assess whether the LLM is heading in the correct reasoning. We enhance the traditional generative task with the retrieval-based framework on feasible options of code coverage. Our experimental results show that CRISPE achieves high accuracy in coverage prediction in terms of both exact-match and statement-match coverage metrics, improving over the baselines. We also show that with semantic-guiding and dynamic reasoning from CRISPE, the LLM generates more correct planning steps. To demonstrate CRISPE’s usefulness, we used it in the downstream task of statically detecting runtime error(s) in incomplete code snippets with the given inputs.

**Link**: [Read Paper](https://doi.org/10.1145/3729401)

**Labels**: [program testing](../../labels/program_testing.md), [general testing](../../labels/general_testing.md)
