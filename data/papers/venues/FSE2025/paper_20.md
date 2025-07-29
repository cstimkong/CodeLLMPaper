# Detecting and Reducing the Factual Hallucinations of Large Language Models with Metamorphic Testing

**Authors**: Wu, Weibin and Cao, Yuhang and Yi, Ning and Ou, Rongyi and Zheng, Zibin

**Abstract**:

Question answering (QA) is a fundamental task of large language models (LLMs), which requires LLMs to automatically answer human-posed questions in natural language. However, LLMs are known to distort facts and make non-factual statements (i.e., hallucinations) when dealing with QA tasks, which may affect the deployment of LLMs in real-life situations. In this work, we propose DrHall, a framework for detecting and reducing the factual hallucinations of black-box LLMs with metamorphic testing (MT). We believe that hallucinated answers are unstable. Therefore, when LLMs hallucinate, they are more likely to produce different answers if we use metamorphic testing to make LLMs re-execute the same task with different execution paths, which motivates the design of DrHall. The effectiveness of DrHall is evaluated empirically on three datasets, including a self-built dataset of natural language questions: FactHalluQA, as well as two datasets of programming questions: Refactory and LeetCode. The evaluation results confirm that DrHall can consistently outperform the state-of-the-art baselines, obtaining an average F1 score of over 0.856 for hallucination detection. For hallucination correction, DrHall can also outperform the state-of-the-art baselines, with an average hallucination correction rate of over 53\%. We hope that our work can enhance the reliability of LLMs and provide new insights for the research of LLM hallucination mitigation.

**Link**: [Read Paper](https://doi.org/10.1145/3715784)

**Labels**: [hallucination in reasoning](../../labels/hallucination_in_reasoning.md)
