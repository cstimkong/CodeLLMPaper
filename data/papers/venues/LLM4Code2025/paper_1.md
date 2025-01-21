# METAMON: Finding Inconsistencies between Program Documentation and Behavior using Metamorphic LLM Queries

**Authors**: Hyeonseok Lee, Gabin An, Shin Yoo

**Abstract**:

Code documentation can, if written precisely, help developers better understand the code they accompany. However, unlike code, code documentation cannot be automatically verified via execution, potentially leading to inconsistencies between documentation and the actual behavior. While such inconsistencies can harmful for developer’s understanding of the code, checking and finding them remains a costly task due to the involvement of human engineers. This paper proposes METAMON, which uses an existing search-based test generation technique to capture the current program behavior in the form of test cases, and subsequently uses LLM-based code reasoning to identify the generated regression test oracles that are not consistent with the program specifications in the documentation. METAMON is supported in this task by metamorphic testing and self-consistency. An empirical evaluation against 9,482 pairs of code documentation and code snippets, generated using five opensource projects from Defects4J v2.0.1, shows that METAMON can classify the code-and-documentation inconsistencies with the precision of 0.72 and the recall of 0.48.

**Link**: [Read Paper](https://coinse.github.io/publications/pdfs/Lee2025aa.pdf)

**Labels**: [program testing](../../labels/program_testing.md), [differential testing](../../labels/differential_testing.md)
