# Automated Unit Test Refactoring

**Authors**: Gao, Yi and Hu, Xing and Yang, Xiaohu and Xia, Xin

**Abstract**:

Test smells arise from poor design practices and insufficient domain knowledge, which can lower the quality of test code and make it harder to maintain and update. Manually refactoring of test smells is time-consuming and error-prone, highlighting the necessity for automated approaches. Current rule-based refactoring methods often struggle in scenarios not covered by predefined rules and lack the flexibility needed to handle diverse cases effectively. In this paper, we propose a novel approach called UTRefactor, a context-enhanced, LLM-based framework for automatic test refactoring in Java projects. UTRefactor extracts relevant context from test code and leverages an external knowledge base that includes test smell definitions, descriptions, and DSL-based refactoring rules. By simulating the manual refactoring process through a chain-of-thought approach, UTRefactor guides the LLM to eliminate test smells in a step-by-step process, ensuring both accuracy and consistency throughout the refactoring. Additionally, we implement a checkpoint mechanism to facilitate comprehensive refactoring, particularly when multiple smells are present. We evaluate UTRefactor on 879 tests from six open-source Java projects, reducing the number of test smells from 2,375 to 265, achieving an 89\% reduction. UTRefactor outperforms direct LLM-based refactoring methods by 61.82\% in smell elimination and significantly surpasses the performance of a rule-based test smell refactoring tool. Our results demonstrate the effectiveness of UTRefactor in enhancing test code quality while minimizing manual involvement.

**Link**: [Read Paper](https://doi.org/10.1145/3715750)

**Labels**: [program testing](../../labels/program_testing.md), [unit testing](../../labels/unit_testing.md), [code generation](../../labels/code_generation.md), [program transformation](../../labels/program_transformation.md)
