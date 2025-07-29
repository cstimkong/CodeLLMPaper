# Few-Shot Natural Language to First-Order Logic Translation via Code Generation

**Authors**: Liu, Junnan

**Abstract**:

Translation of natural language to first-order logical formula (NL-FOL) has recently gained significant attention for its critical role in logic-based NLP applications. Some studies attempt to utilize pretrained language models in a sequence-to-sequence manner for the NL-FOL task. However, these methods encounter challenges such as (1) inconsistency between the training and inference phases and (2) the data-intensive and resource-intensive finetuning process. This paper introduces a novel NL-FOL translation method, dubbed Code4Logic, which is based on in-context learning and employs code snippets to bridge the gap between natural language and first-order logic. By converting the translation task into a progressive code generation task, Code4Logic demonstrates strong generalization within a training-free manner, and enhances the performance of large language models (LLMs) to generate complex first-order logical formulas. Experimental results on NL-FOL task and downstream task datasets indicate that Code4Logic surpasses prominent training-free baselines and is comparable to supervised models trained on the full training data.

**Link**: [Read Paper](https://aclanthology.org/2025.naacl-long.547/)

**Labels**: [code generation](../../labels/code_generation.md), [program synthesis](../../labels/program_synthesis.md)
