# {PLEX}: Adaptive Parameter-Efficient Fine-Tuning for Code {LLM}s using Lottery-Tickets

**Authors**: Lee, Jaeseong  and    Han, Hojae  and    Kim, Jongyoon  and    Hwang, Seung-won  and    Kang, Naun  and    An, KyungJun  and    Jang, Sungho

**Abstract**:

Fine-tuning large language models (LLMs) for code generation is challenging due to computational costs and the underrepresentation of some programming languages (PLs) in pre-training. We propose PLEX, a lottery-ticket based parameter-efficient fine-tuning (PEFT) method that adapts LLMs to either well-supported and underrepresented PLs.During lottery ticket selection, PLEX employs a dual strategy: for well-represented PLs, it leverages the LLM{'}s full parametric knowledge by selecting from full layers, while for underrepresented PLs, it narrows the selection scope to dense layers, prioritizing the most influential parameters.Additionally, PLEX-E, a low-rank extension of PLEX, further reduces computational costs by limiting the scope of fine-tuning. On MultiPL-E benchmarks, PLEX achieves state-of-the-art performance among PEFT methods, while PLEX-E maintains competitive results with reduced computational overhead. Both variants demonstrate effective adaptation across diverse programming languages, particularly for those underrepresented in pre-training.

**Link**: [Read Paper](https://aclanthology.org/2025.naacl-industry.60/)

**Labels**: [code generation](../../labels/code_generation.md), [program synthesis](../../labels/program_synthesis.md), [code model](../../labels/code_model.md), [code model training](../../labels/code_model_training.md)
