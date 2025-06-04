# DiffSpec: Differential Testing with LLMs using Natural Language Specifications and Code Artifacts

**Authors**: Nikitha Rao, Elizabeth Gilbert, Tahina Ramananandro, Nikhil Swamy, Claire Le Goues, Sarah Fakhoury

**Abstract**:

Differential testing can be an effective way to find bugs in software systems with multiple implementations that conform to the same specification, like compilers, network protocol parsers, and language runtimes. Specifications for such systems are often standardized in natural language documents, like Instruction Set Architecture (ISA) specifications, Wasm specifications or IETF RFC's. Large Language Models (LLMs) have demonstrated potential in both generating tests and handling large volumes of natural language text, making them well-suited for utilizing artifacts like specification documents, bug reports, and code implementations. In this work, we leverage natural language and code artifacts to guide LLMs to generate targeted, meaningful tests that highlight meaningful behavioral differences between implementations, including those corresponding to bugs. We introduce DiffSpec, a framework for generating differential tests with LLMs using prompt chaining. We demonstrate the efficacy of DiffSpec on two different systems, namely, eBPF runtimes and Wasm validators. Using DiffSpec, we generated 359 differentiating tests, uncovering at least four distinct and confirmed bugs in eBPF, including a kernel memory leak, inconsistent behavior in jump instructions, and undefined behavior when using the stack pointer. We also found 279 differentiating tests in Wasm validators, that point to at least 2 confirmed and fixed bugs in Wizard Engine.

**Link**: [Read Paper](https://arxiv.org/abs/2410.04249)

**Labels**: [program testing](../../labels/program_testing.md), [differential testing](../../labels/differential_testing.md), [static analysis](../../labels/static_analysis.md), [specification inference](../../labels/specification_inference.md)
