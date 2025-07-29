# Investigating the Transferability of Code Repair for Low-Resource Programming Languages

**Authors**: Wong, Kyle  and      Amayuelas, Alfonso  and      Pan, Liangming  and      Wang, William Yang

**Abstract**:

Large language models (LLMs) have shown remarkable performance on code generation tasks. A recent use case is iterative code repair, where an LLM fixes an incorrect program by rationalizing about errors and generating new code. Recent works augment the code repair process by integrating modern techniques such as chain-of-thought reasoning or distillation, but only study their benefits on high-resource languages like Python, and ignore low-resource languages like Perl. To address this gap of knowledge, we investigate the benefits of distilling code repair for both high and low resource languages to determine if the techniques that are effective in a high resource setting are also applicable in a low resource setting. Our evaluation shows that distilling the ability to repair code has language dependent benefits. To explain this behavior, we perform a further analysis and find that contrary to preexisting beliefs, the correlation between reasoning ability and code correction ability is weak. We hypothesize this weak correlation is magnified in low-resource settings where base models lack deep knowledge of a programming language, leading to wavering benefits of code repair.

**Link**: [Read Paper](https://aclanthology.org/2025.findings-naacl.190/)

**Labels**: [code generation](../../labels/code_generation.md), [program repair](../../labels/program_repair.md), [empirical study](../../labels/empirical_study.md)
