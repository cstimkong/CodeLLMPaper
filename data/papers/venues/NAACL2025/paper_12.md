# {COAST}: Enhancing the Code Debugging Ability of {LLM}s through Communicative Agent Based Data Synthesis

**Authors**: Yang, Weiqing  and      Wang, Hanbin  and      Liu, Zhenghao  and      Li, Xinze  and      Yan, Yukun  and      Wang, Shuo  and      Gu, Yu  and      Yu, Minghe  and      Liu, Zhiyuan  and      Yu, Ge

**Abstract**:

Code debugging is a vital stage of software development, essential for ensuring the reliability and performance of Large Language Models (LLMs) in the code generation task. Human debugging typically follows a multi-stage process, which includes Bug Localization, Bug Identification, Code Repair, and Code Recognition. However, existing code debugging benchmarks predominantly focus on the Code Repair stage, which offers only a limited perspective on evaluating the debugging capabilities of LLMs. In this paper, we introduce DEBUGEVAL, a comprehensive benchmark for evaluating the debugging abilities of LLMs by emulating the multi-stage human debugging process. Through evaluating on DEBUGEVAL, we observe that 7B-scale models consistently underperform compared to their larger counterparts, highlighting their limitations in comprehending code semantics. In this case, we propose the COmmunicative Agent-based data SynThesis (COAST) framework, which employs a multi-agent system to generate high-quality training data for supervised fine-tuning (SFT). Experimental results demonstrate that COAST-generated data outperform human-curated and GPT-4-generated data, enabling 7B-scale LLMs to achieve debugging performance comparable to GPT-3.5. All data and codes are available at https://github.com/NEUIR/COAST.

**Link**: [Read Paper](https://aclanthology.org/2025.findings-naacl.139/)

**Labels**: [program testing](../../labels/program_testing.md), [debugging](../../labels/debugging.md), [agent design](../../labels/agent_design.md), [code model](../../labels/code_model.md), [code model training](../../labels/code_model_training.md)
