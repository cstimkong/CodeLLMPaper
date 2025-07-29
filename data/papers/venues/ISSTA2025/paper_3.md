# Beyond Static Pattern Matching? Rethinking Automatic Cryptographic API Misuse Detection in the Era of LLMs

**Authors**: Xia, Yifan and Xie, Zichen and Liu, Peiyu and Lu, Kangjie and Liu, Yan and Wang, Wenhai and Ji, Shouling

**Abstract**:

While the automated detection of cryptographic API misuses has progressed significantly, its precision diminishes for intricate targets due to the reliance on manually defined patterns. Large Language Models (LLMs) offer a promising context-aware understanding to address this shortcoming, yet the stochastic nature and the hallucination issue pose challenges to their applications in precise security analysis. This paper presents the first systematic study to explore LLMs’ application in cryptographic API misuse detection. Our findings are noteworthy: The instability of directly applying LLMs results in over half of the initial reports being false positives. Despite this, the reliability of LLM-based detection could be significantly enhanced by aligning detection scopes with realistic scenarios and employing a novel code \&amp; analysis validation technique, achieving a nearly 90\% detection recall. This improvement substantially surpasses traditional methods and leads to the discovery of previously unknown vulnerabilities in established benchmarks. Nevertheless, we identify recurring failure patterns that illustrate current LLMs’ blind spots, including cryptographic knowledge deficiencies and code semantics misinterpretations. Leveraging these findings, we deploy an LLM-based detection system and uncover 63 new vulnerabilities (47 confirmed, 7 already fixed) in open-source Java and Python repositories, including prominent projects like Apache.

**Link**: [Read Paper](https://doi.org/10.1145/3728875)

**Labels**: [static analysis](../../labels/static_analysis.md), [bug detection](../../labels/bug_detection.md)
