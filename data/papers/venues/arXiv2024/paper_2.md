# An Empirical Study of Large Language Models for Type and Call Graph Analysis

**Authors**: Ashwin Prasad Shivarpatna Venkatesh, Rose Sunil, Samkutty Sabu, Amir M. Mir, Sofia Reis, Eric Bodden

**Abstract**:

Large Language Models (LLMs) are increasingly being explored for their potential in software engineering, particularly in static analysis tasks. In this study, we investigate the potential of current LLMs to enhance call-graph analysis and type inference for Python and JavaScript programs. We empirically evaluated 24 LLMs, including OpenAI's GPT series and open-source models like LLaMA and Mistral, using existing and newly developed benchmarks. Specifically, we enhanced TypeEvalPy, a micro-benchmarking framework for type inference in Python, with auto-generation capabilities, expanding its scope from 860 to 77,268 type annotations for Python. Additionally, we introduced SWARM-CG and SWARM-JS, comprehensive benchmarking suites for evaluating call-graph construction tools across multiple programming languages. Our findings reveal a contrasting performance of LLMs in static analysis tasks. For call-graph generation in Python, traditional static analysis tools like PyCG significantly outperform LLMs. In JavaScript, the static tool TAJS underperforms due to its inability to handle modern language features, while LLMs, despite showing potential with models like mistral-large-it-2407-123b and GPT-4o, struggle with completeness and soundness in both languages for call-graph analysis. Conversely, LLMs demonstrate a clear advantage in type inference for Python, surpassing traditional tools like HeaderGen and hybrid approaches such as HiTyper. These results suggest that while LLMs hold promise in type inference, their limitations in call-graph analysis highlight the need for further research. Our study provides a foundation for integrating LLMs into static analysis workflows, offering insights into their strengths and current limitations.

**Link**: [Read Paper](https://arxiv.org/abs/2410.00603)

**Labels**: [static analysis](../../labels/static_analysis.md), [type inference](../../labels/type_inference.md), [call graph analysis](../../labels/call_graph_analysis.md)
