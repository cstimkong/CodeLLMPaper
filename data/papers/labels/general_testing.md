# General Testing

- [Blended Analysis for Predictive Execution](../venues/FSE2025/paper_40.md), ([FSE2025](../venues/FSE2025/README.md))

  - **Abstract**: Although Large Language Models (LLMs) are highly proficient in understanding source code and descriptive texts, they have limitations in reasoning on dynamic program behaviors, such as execution trace and code coverage prediction, and runtime error prediction, which usually require actual program execution. To advance the ability of LLMs in predicting dynamic behaviors, we leverage the strengths of both approaches, Program Analysis (PA) and LLM, in building PredEx, a predictive executor for Pyth...
  - **Labels**: [program testing](program_testing.md), [general testing](general_testing.md)


- [CRISPE: Semantic-Guided Execution Planning and Dynamic Reasoning for Enhancing Code Coverage Prediction](../venues/FSE2025/paper_39.md), ([FSE2025](../venues/FSE2025/README.md))

  - **Abstract**: While LLMs excel in understanding source code and descriptive texts for tasks like code generation, code completion, etc., they exhibit weaknesses in predicting dynamic program behavior, such as code coverage and runtime error detection, which typically require program execution. Aiming to advance the capability of LLMs in reasoning and predicting the program behavior at runtime, we present CRISPE (short for Coverage Rationalization and Intelligent Selection ProcedurE), a novel approach for code...
  - **Labels**: [program testing](program_testing.md), [general testing](general_testing.md)


- [CoverUp: Effective High Coverage Test Generation for Python](../venues/FSE2025/paper_36.md), ([FSE2025](../venues/FSE2025/README.md))

  - **Abstract**: Testing is an essential part of software development. Test generation tools attempt to automate the otherwise labor-intensive task of test creation, but generating high-coverage tests remains challenging. This paper proposes CoverUp, a novel approach to driving the generation of high-coverage Python regression tests. CoverUp combines coverage analysis, code context, and feedback in prompts that iteratively guide the LLM to generate tests that improve line and branch coverage.   We evaluate our p...
  - **Labels**: [program testing](program_testing.md), [general testing](general_testing.md)


- [Doc2OracLL: Investigating the Impact of Documentation on LLM-Based Test Oracle Generation](../venues/FSE2025/paper_23.md), ([FSE2025](../venues/FSE2025/README.md))

  - **Abstract**: Code documentation is a critical artifact of software development, bridging human understanding and machine-   readable code. Beyond aiding developers in code comprehension and maintenance, documentation also plays   a critical role in automating various software engineering tasks, such as test oracle generation (TOG). In Java,   Javadoc comments offer structured, natural language documentation embedded directly within the source   code, typically describing functionality, usage, parameters, ret...
  - **Labels**: [program testing](program_testing.md), [general testing](general_testing.md), [empirical study](empirical_study.md)


- [Tratto: A Neuro-Symbolic Approach to Deriving Axiomatic Test Oracles](../venues/ISSTA2025/paper_28.md), ([ISSTA2025](../venues/ISSTA2025/README.md))

  - **Abstract**: This paper presents Tratto, a neuro-symbolic approach that generates assertions (boolean expressions) that can serve as axiomatic oracles, from source code and documentation. The symbolic module of Tratto takes advantage of the grammar of the programming language, the unit under test, and the context of the unit (its class and available APIs) to restrict the search space of the tokens that can be successfully used to generate valid oracles. The neural module of Tratto uses transformers fine-tune...
  - **Labels**: [program testing](program_testing.md), [general testing](general_testing.md)


- [You Name It, I Run It: An LLM Agent to Execute Tests of Arbitrary Projects](../venues/ISSTA2025/paper_1.md), ([ISSTA2025](../venues/ISSTA2025/README.md))

  - **Abstract**: The ability to execute the test suite of a project is essential in many scenarios, e.g., to assess code quality and code coverage, to validate code changes made by developers or automated tools, and to ensure compatibility with dependencies. Despite its importance, executing the test suite of a project can be challenging in practice because different projects use different programming languages, software ecosystems, build systems, testing frameworks, and other tools. These challenges make it dif...
  - **Labels**: [program testing](program_testing.md), [general testing](general_testing.md), [agent design](agent_design.md)


- [exLong: Generating Exceptional Behavior Tests with Large Language Models](../venues/ICSE2025/paper_51.md), ([ICSE2025](../venues/ICSE2025/README.md))

  - **Abstract**: Many popular programming languages, including C#, Java, and Python, support exceptions. Exceptions are thrown during program execution if an unwanted event happens, e.g., a method is invoked with an illegal argument value. Software developers write exceptional behavior tests (EBTs) to check that their code detects unwanted events and throws appropriate exceptions. Prior research studies have shown the importance of EBTs, but those studies also highlighted that developers put most of their effort...
  - **Labels**: [program testing](program_testing.md), [general testing](general_testing.md)
