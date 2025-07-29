# ChatDBG: Augmenting Debugging with Large Language Models

**Authors**: Levin, Kyla H. and van Kempen, Nicolas and Berger, Emery D. and Freund, Stephen N.

**Abstract**:

Debugging is a critical but challenging task for programmers. This paper proposes ChatDBG, an AI-powered debugging assistant. ChatDBG integrates large language models (LLMs) to significantly enhance the capabilities and user-friendliness of conventional debuggers. ChatDBG lets programmers engage in a collaborative dialogue with the debugger, allowing them to pose complex questions about program state, perform root cause analysis for crashes or assertion failures, and explore open-ended queries like "why is x null?". To handle these queries, ChatDBG grants the LLM autonomy to "take the wheel": it can act as an independent agent capable of querying and controlling the debugger to navigate through stacks and inspect program state. It then reports its findings and yields back control to the programmer. By leveraging the real-world knowledge embedded in LLMs, ChatDBG can diagnose issues identifiable only through the use of domain-specific reasoning. Our ChatDBG prototype integrates with standard debuggers including LLDB and GDB for native code and Pdb for Python. Our evaluation across a diverse set of code, including C/C++ code with known bugs and a suite of Python code including standalone scripts and Jupyter notebooks, demonstrates that ChatDBG can successfully analyze root causes, explain bugs, and generate accurate fixes for a wide range of real-world errors. For the Python programs, a single query led to an actionable bug fix 67\% of the time; one additional follow-up query increased the success rate to 85\%. ChatDBG has seen rapid uptake; it has already been downloaded more than 75,000 times.

**Link**: [Read Paper](https://doi.org/10.1145/3729355)

**Labels**: [program testing](../../labels/program_testing.md), [debugging](../../labels/debugging.md)
