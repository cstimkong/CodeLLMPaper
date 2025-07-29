# Enhancing Automated Loop Invariant Generation for Complex Programs with Large Language Models

**Authors**: Ruibang Liu, Guoqiang Li, Minyu Chen, Ling-I Wu, Jingyu Ke

**Abstract**:

Automated program verification has always been an important component of building trustworthy software. While the analysis of real-world programs remains a theoretical challenge, the automation of loop invariant analysis has effectively resolved the problem. However, real-world programs that often mix complex data structures and control flows pose challenges to traditional loop invariant generation tools. To enhance the applicability of invariant generation techniques, we proposed ACInv, an Automated Complex program loop Invariant generation tool, which combines static analysis with Large Language Models (LLMs) to generate the proper loop invariants. We utilize static analysis to extract the necessary information for each loop and embed it into prompts for the LLM to generate invariants for each loop. Subsequently, we employ an LLM-based evaluator to assess the generated invariants, refining them by either strengthening, weakening, or rejecting them based on their correctness, ultimately obtaining enhanced invariants. We conducted experiments on ACInv, which showed that ACInv outperformed previous tools on data sets with data structures, and maintained similar performance to the state-of-the-art tool AutoSpec on numerical programs without data structures. For the total data set, ACInv can solve 21% more examples than AutoSpec and can generate reference data structure templates.

**Link**: [Read Paper](https://arxiv.org/pdf/2412.10483)

**Labels**: [static analysis](../../labels/static_analysis.md), [program verification](../../labels/program_verification.md)
