# Integrating Large Language Models and Reinforcement Learning for Non-linear Reasoning

**Authors**: Alon, Yoav and David, Cristina

**Abstract**:

Large Language Models (LLMs) were shown to struggle with long-term planning, which may be caused by the limited way in which they explore the space of possible solutions. We propose an architecture where a Reinforcement Learning (RL) Agent guides an LLM's space exploration: (1) the Agent has access to domain-specific information, and can therefore make decisions about the quality of candidate solutions based on specific and relevant metrics, which were not explicitly considered by the LLM's training objective; (2) the LLM can focus on generating immediate next steps, without the need for long-term planning. We allow non-linear reasoning by exploring alternative paths and backtracking. We evaluate this architecture on the program equivalence task, and compare it against Chain of Thought (CoT) and Tree of Thoughts (ToT). We assess both the downstream task, denoting the binary classification, and the intermediate reasoning steps. Our approach compares positively against CoT and ToT.

**Link**: [Read Paper](https://doi.org/10.1145/3715761)

**Labels**: [agent design](../../labels/agent_design.md), [planning](../../labels/planning.md), [hallucination in reasoning](../../labels/hallucination_in_reasoning.md)
