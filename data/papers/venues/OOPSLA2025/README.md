# OOPSLA2025

Number of papers: 2

## [Artemis: Toward Accurate Detection of Server-Side Request Forgeries through LLM-Assisted Inter-procedural Path-Sensitive Taint Analysis](paper_1.md)
- **Authors**: Yuchen Ji, Ting Dai, Zhichao Zhou, Yutian Tang, Jingzhu He
- **Abstract**: Server-side request forgery (SSRF) vulnerabilities are inevitable in PHP web applications. Existing static tools in detecting vulnerabilities in PHP web applications neither contain SSRF-related features to enhance detection accuracy nor consider PHP’s dynamic type features. In this paper, we present Artemis, a static taint analysis tool for detecting SSRF vulnerabilities in PHP web applications. First, Artemis extracts both PHP built-in and third-party functions as candidate source and sink fun...
- **Link**: [Read Paper](https://dl.acm.org/doi/10.1145/3720488)
- **Labels**: [static analysis](../../labels/static_analysis.md), [bug detection](../../labels/bug_detection.md)


## [Laurel: Unblocking Automated Verification with Large Language Models](paper_2.md)
- **Authors**: YEric Mugnier, Emmanuel Anaya Gonzalez, Nadia Polikarpova, Ranjit Jhala, Zhou Yuanyuan
- **Abstract**: Program verifiers such as Dafny automate proofs by outsourcing them to an SMT solver. This automation is not perfect, however, and the solver often requires hints in the form of assertions, creating a burden for the proof engineer. In this paper, we propose, a tool that alleviates this burden by automatically generating assertions using large language models (LLMs). To improve the success rate of LLMs in this task, we design two domain-specific prompting techniques. First, we help the LLM determ...
- **Link**: [Read Paper](https://dl.acm.org/doi/10.1145/3720499)
- **Labels**: [static analysis](../../labels/static_analysis.md), [program verification](../../labels/program_verification.md)
