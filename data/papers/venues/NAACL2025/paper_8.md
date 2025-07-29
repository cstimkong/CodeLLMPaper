# {DCE}-{LLM}: Dead Code Elimination with Large Language Models

**Authors**: Chen, Minyu  and      Li, Guoqiang  and      Wu, Ling-I  and      Liu, Ruibang

**Abstract**:

Dead code introduces several challenges in software development, such as increased binary size and maintenance difficulties. It can also obscure logical errors and be exploited for obfuscation in malware. For LLM-based code-related tasks, dead code introduces vulnerabilities that can mislead these models, raising security concerns. Although modern compilers and IDEs offer dead code elimination, sophisticated patterns can bypass these tools. A universal approach that includes classification, location, explanation, and correction is needed, yet current tools often require significant manual effort. We present DCE-LLM, a framework for automated dead code elimination using a small CodeBERT model with an attribution-based line selector to efficiently locate suspect code. LLMs then generate judgments and explanations, fine-tuned on a large-scale, annotated dead code dataset to provide detailed explanations and patches. DCE-LLM outperforms existing tools, with advanced unreachability detection, automated correction, and support for multiple programming languages. Experimental results show DCE-LLM achieves over 94{\%} F1 scores for unused and unreachable code, significantly surpassing GPT-4o by 30{\%}.

**Link**: [Read Paper](https://aclanthology.org/2025.naacl-long.501/)

**Labels**: [static analysis](../../labels/static_analysis.md), [bug detection](../../labels/bug_detection.md), [program optimization](../../labels/program_optimization.md)
