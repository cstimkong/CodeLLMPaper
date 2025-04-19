# Artemis: Toward Accurate Detection of Server-Side Request Forgeries through LLM-Assisted Inter-procedural Path-Sensitive Taint Analysis

**Authors**: Yuchen Ji, Ting Dai, Zhichao Zhou, Yutian Tang, Jingzhu He

**Abstract**:

Server-side request forgery (SSRF) vulnerabilities are inevitable in PHP web applications. Existing static tools in detecting vulnerabilities in PHP web applications neither contain SSRF-related features to enhance detection accuracy nor consider PHP’s dynamic type features. In this paper, we present Artemis, a static taint analysis tool for detecting SSRF vulnerabilities in PHP web applications. First, Artemis extracts both PHP built-in and third-party functions as candidate source and sink functions. Second, Artemis constructs both explicit and implicit call graphs to infer functions’ relationships. Third, Artemis performs taint analysis based on a set of rules that prevent over-tainting and pauses when SSRF exploitation is impossible. Fourth, Artemis analyzes the compatibility of path conditions to prune false positives. We have implemented a prototype of Artemis and evaluated it on 250 PHP web applications. Artemis reports 207 true vulnerable paths (106 true SSRFs) with 15 false positives. Of the 106 detected SSRFs, 35 are newly found and reported to developers, with 24 confirmed and assigned CVE IDs.

**Link**: [Read Paper](https://dl.acm.org/doi/10.1145/3720488)

**Labels**: [static analysis](../../labels/static_analysis.md), [bug detection](../../labels/bug_detection.md)
