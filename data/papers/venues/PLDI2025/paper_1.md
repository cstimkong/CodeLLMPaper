# DR.FIX: Automatically Fixing Data Races at Industry Scale

**Authors**: Farnaz Behrang, Zhizhou Zhang, Georgian-Vlad Saioc, Peng Liu, Milind Chabbi

**Abstract**:

Data races are a prevalent class of concurrency bugs in shared-memory parallel programs, posing significant challenges to software reliability and reproducibility. While there is an extensive body of research on detecting data races and a wealth of practical detection tools across various programming languages, considerably less effort has been directed toward automatically fixing data races at an industrial scale. In large codebases, data races are continuously introduced and exhibit myriad patterns, making automated fixing particularly challenging. In this paper, we tackle the problem of automatically fixing data races at an industrial scale. We present this http URL, a tool that combines large language models (LLMs) with program analysis to generate fixes for data races in real-world settings, effectively addressing a broad spectrum of racy patterns in complex code contexts. Implemented for Go--the programming language widely used in modern microservice architectures where concurrency is pervasive and data races are this http URL seamlessly integrates into existing development workflows. We detail the design of this http URL and examine how individual design choices influence the quality of the fixes produced. Over the past 18 months, this http URL has been integrated into developer workflows at Uber demonstrating its practical utility. During this period, this http URL produced patches for 224 (55%) from a corpus of 404 data races spanning various categories; 193 of these patches (86%) were accepted by more than a hundred developers via code reviews and integrated into the codebase.

**Link**: [Read Paper](https://arxiv.org/abs/2504.15637)

**Labels**: [code generation](../../labels/code_generation.md), [program repair](../../labels/program_repair.md)
