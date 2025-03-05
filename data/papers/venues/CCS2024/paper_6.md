# Repairing Bugs with the Introduction of New Variables: A Multi-Agent Large Language Model

**Authors**: Zhang, Elisa and Sun, Shiyu and Xing, Yunlong and Sun, Kun

**Abstract**:

Trained on billions of tokens, large language models (LLMs) have a broad range of empirical knowledge which enables them to generate software patches with complex repair patterns. We leverage the powerful code-fixing capabilities of LLMs and propose VarPatch, a multi-agent conversational automated program repair (APR) technique that iteratively queries the LLM to generate software patches by providing various prompts and context information. VarPatch focuses on the variable addition repair pattern, as previous APR tools struggle to introduce and use new variables to fix buggy code. Additionally, we summarize commonly used APIs and identify four repair patterns involving new variable addition. Our evaluation on the Defects4J 1.2 dataset shows that VarPatch can repair 69\% more bugs than baseline tools and over 8 times more bugs than GPT-4.

**Link**: [Read Paper](https://doi.org/10.1145/3658644.3691412)

**Labels**: [code generation](../../labels/code_generation.md), [program repair](../../labels/program_repair.md)
