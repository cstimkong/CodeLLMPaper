# Compiler Testing

- [Clozemaster: Fuzzing Rust Compiler by Harnessing Llms for Infilling Masked Real Programs](../venues/ICSE2025/paper_50.md), ([ICSE2025](../venues/ICSE2025/README.md))

  - **Abstract**: Ensuring the reliability of the Rust compiler is of paramount importance, given increasing adoption of Rust for critical systems development, due to its emphasis on memory and thread safety. However, generating valid test programs for the Rust compiler poses significant challenges, given Rust's complex syntax and strict requirements. With the growing popularity of large language models (LLMs), much research in software testing has explored using LLMs to generate test cases. Still, directly using...
  - **Labels**: [program testing](program_testing.md), [fuzzing](fuzzing.md), [compiler testing](compiler_testing.md)


- [Fuzzing JavaScript Interpreters with Coverage-Guided Reinforcement Learning for LLM-Based Mutation](../venues/ISSTA2024/paper_22.md), ([ISSTA2024](../venues/ISSTA2024/README.md))

  - **Abstract**: JavaScript interpreters, crucial for modern web browsers, require an effective fuzzing method to identify security-related bugs. However, the strict grammatical requirements for input present significant challenges. Recent efforts to integrate language models for context- aware mutation in fuzzing are promising but lack the necessary coverage guidance to be fully effective. This paper presents a novel technique called CovRL (Coverage-guided Reinforcement Learning) that combines Large Language Mo...
  - **Labels**: [program testing](program_testing.md), [fuzzing](fuzzing.md), [compiler testing](compiler_testing.md)


- [LLM-Based Code Generation Method for Golang Compiler Testing](../venues/FSE2023/paper_7.md), ([FSE2023](../venues/FSE2023/README.md))

  - **Abstract**: Modern optimizing compilers are among the most complex software systems humans build. One way to identify subtle compiler bugs is fuzzing. Both the quantity and the quality of testcases are crucial to the performance of fuzzing. Traditional testcase-generation methods, such as Csmith and YARPGen, have been proven successful at discovering compiler bugs. However, such generated testcases have limited coverage and quantity. In this paper, we present a code generation method for compiler testing ba...
  - **Labels**: [program testing](program_testing.md), [fuzzing](fuzzing.md), [compiler testing](compiler_testing.md)


- [The Mutators Reloaded: Fuzzing Compilers with Large Language Model Generated Mutation Operators](../venues/ASPLOS2024/paper_1.md), ([ASPLOS2024](../venues/ASPLOS2024/README.md))

  - **Abstract**: Crafting high-quality mutators–the core of mutation-based fuzzing that shapes the search space–is challenging. It requires human expertise and creativity, and their implementation demands knowledge of compiler internals. This paper presents MetaMut framework for developing new, useful mutators for compiler fuzzing. It integrates our compilerdomain knowledge into prompts and processes that can best harness the capabilities of a large language model. With MetaMut, we have successfully created 118 ...
  - **Labels**: [program testing](program_testing.md), [fuzzing](fuzzing.md), [compiler testing](compiler_testing.md)


- [WhiteFox: White-Box Compiler Fuzzing Empowered by Large Language Models](../venues/OOPSLA2024/paper_3.md), ([OOPSLA2024](../venues/OOPSLA2024/README.md))

  - **Abstract**: Compiler correctness is crucial, as miscompilation can falsify program behaviors, leading to serious consequences over the software supply chain. In the literature, fuzzing has been extensively studied to uncover compiler defects. However, compiler fuzzing remains challenging: Existing arts focus on black- and grey-box fuzzing, which generates test programs without sufficient understanding of internal compiler behaviors. As such, they often fail to construct test programs to exercise intricate o...
  - **Labels**: [program testing](program_testing.md), [fuzzing](fuzzing.md), [compiler testing](compiler_testing.md)
