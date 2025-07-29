# Benchmarking Language Model Creativity: A Case Study on Code Generation

**Authors**: Lu, Yining  and      Wang, Dixuan  and      Li, Tianjian  and      Jiang, Dongwei  and      Khudanpur, Sanjeev  and      Jiang, Meng  and      Khashabi, Daniel

**Abstract**:

As LLMs become increasingly prevalent, it is interesting to consider how ``creative'' these models can be. From cognitive science, creativity consists of at least two key characteristics: \textit{convergent} thinking (purposefulness to achieve a given goal) and \textit{divergent} thinking (adaptability to explore new environments or constraints) (CITATION). In this work, we introduce a framework for quantifying LLM creativity that incorporates the two design ingredients: (1) We introduce DENIAL PROMPTING which pushes LLMs to develop more creative solutions to a given problem by incrementally imposing new constraints on the previous solution, compelling LLMs to adopt new strategies. (2) We define NEOGAUGE, a metric that quantifies both convergent and divergent thinking in the generated creative responses by LLMs. We test the proposed framework on Codeforces problems, which serve as both a natural dataset for coding tasks and a collection of prior human solutions. We quantify NEOGAUGE for various proprietary and open-source models and find that even the most creative model, GPT-4, still falls short of demonstrating human-like creativity. We also experiment with advanced reasoning strategies (MCTS, self-correction, etc.) and observe no significant improvement in creativity. As a by-product of our analysis, we release NEOCODER dataset for reproducing our results on future models.

**Link**: [Read Paper](https://aclanthology.org/2025.naacl-long.141/)

**Labels**: [code generation](../../labels/code_generation.md), [program synthesis](../../labels/program_synthesis.md), [benchmark](../../labels/benchmark.md)
