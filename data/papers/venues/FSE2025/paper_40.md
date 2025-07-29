# Blended Analysis for Predictive Execution

**Authors**: Li, Yi and Dhulipala, Hridya and Yadavally, Aashish and Rong, Xiaokai and Wang, Shaohua and Nguyen, Tien N.

**Abstract**:

Although Large Language Models (LLMs) are highly proficient in understanding source code and descriptive texts, they have limitations in reasoning on dynamic program behaviors, such as execution trace and code coverage prediction, and runtime error prediction, which usually require actual program execution. To advance the ability of LLMs in predicting dynamic behaviors, we leverage the strengths of both approaches, Program Analysis (PA) and LLM, in building PredEx, a predictive executor for Python. Our principle is a blended analysis between PA and LLM to use PA to guide the LLM in predicting execution traces. We break down the task of predictive execution into smaller sub-tasks and leverage the deterministic nature when an execution order can be deterministically decided. When it is not certain, we use predictive backward slicing per variable, i.e., slicing the prior trace to only the parts that affect each variable separately breaks up the valuation prediction into significantly simpler problems. Our empirical evaluation on real-world datasets shows that PredEx achieves 31.5–47.1\% relatively higher accuracy in predicting full execution traces than the state-of-the-art models. It also produces 8.6–53.7\% more correct execution trace prefixes than those baselines. In predicting next executed statements, its relative improvement over the baselines is 15.7–102.3\%. Finally, we show PredEx’s usefulness in two tasks: static code coverage analysis and static prediction of run-time errors for (in)complete code.

**Link**: [Read Paper](https://doi.org/10.1145/3729402)

**Labels**: [program testing](../../labels/program_testing.md), [general testing](../../labels/general_testing.md)
