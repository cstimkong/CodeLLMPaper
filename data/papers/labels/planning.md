# Planning

- [A Pair Programming Framework for Code Generation via Multi-Plan Exploration and Feedback-Driven Refinement](../venues/ASE2024/paper_21.md), ([ASE2024](../venues/ASE2024/README.md))

  - **Abstract**: Large language models (LLMs) have achieved impressive performance on code generation. Although prior studies enhanced LLMs with prompting techniques and code refinement, they still struggle with complex programming problems due to rigid solution plans. In this paper, we draw on pair programming practices to propose PairCoder, a novel LLM-based framework for code generation. PairCoder incorporates two collaborative LLM agents, namely a Navigator agent for high-level planning and a Driver agent fo...
  - **Labels**: [code generation](code_generation.md), [program synthesis](program_synthesis.md), [agent design](agent_design.md), [planning](planning.md)


- [CodePlan: Repository-Level Coding using LLMs and Planning](../venues/FSE2024/paper_20.md), ([FSE2024](../venues/FSE2024/README.md))

  - **Abstract**: Software engineering activities such as package migration, fixing error reports from static analysis or testing, and adding type annotations or other specifications to a codebase, involve pervasively editing the entire repository of code.     We formulate these activities as repository-level coding tasks.         Recent tools like GitHub Copilot, which are powered by Large Language Models (LLMs), have succeeded in offering high-quality solutions to localized coding problems.     Repository-level...
  - **Labels**: [code generation](code_generation.md), [program synthesis](program_synthesis.md), [agent design](agent_design.md), [planning](planning.md)


- [Experiential Co-Learning of Software-Developing Agents](../venues/ACL2024/paper_19.md), ([ACL2024](../venues/ACL2024/README.md))

  - **Abstract**: Recent advancements in large language models (LLMs) have brought significant changes to various domains, especially through LLM-driven autonomous agents. A representative scenario is in software development, where LLM agents demonstrate efficient collaboration, task division, and assurance of software quality, markedly reducing the need for manual involvement. However, these agents frequently perform a variety of tasks independently, without benefiting from past experiences, which leads to repea...
  - **Labels**: [general coding task](general_coding_task.md), [agent design](agent_design.md), [planning](planning.md)


- [Instruct, Not Assist: LLM-based Multi-Turn Planning and Hierarchical Questioning for Socratic Code Debugging](../venues/EMNLP2024/paper_10.md), ([EMNLP2024](../venues/EMNLP2024/README.md))

  - **Abstract**: Socratic questioning is an effective teaching strategy, encouraging critical thinking and problem-solving. The conversational capabilities of large language models (LLMs) show great potential for providing scalable, real-time student guidance. However, current LLMs often give away solutions directly, making them ineffective instructors. We tackle this issue in the code debugging domain with TreeInstruct, an Instructor agent guided by a novel state space-based planning algorithm. TreeInstruct ask...
  - **Labels**: [program testing](program_testing.md), [debugging](debugging.md), [agent design](agent_design.md), [planning](planning.md)


- [Integrating Large Language Models and Reinforcement Learning for Non-linear Reasoning](../venues/FSE2025/paper_13.md), ([FSE2025](../venues/FSE2025/README.md))

  - **Abstract**: Large Language Models (LLMs) were shown to struggle with long-term planning, which may be caused by the limited way in which they explore the space of possible solutions. We propose an architecture where a Reinforcement Learning (RL) Agent guides an LLM's space exploration: (1) the Agent has access to domain-specific information, and can therefore make decisions about the quality of candidate solutions based on specific and relevant metrics, which were not explicitly considered by the LLM's trai...
  - **Labels**: [agent design](agent_design.md), [planning](planning.md), [hallucination in reasoning](hallucination_in_reasoning.md)


- [LocAgent: Graph-Guided LLM Agents for Code Localization](../venues/ACL2025/paper_1.md), ([ACL2025](../venues/ACL2025/README.md))

  - **Abstract**: Code localization--identifying precisely where in a codebase changes need to be made--is a fundamental yet challenging task in software maintenance. Existing approaches struggle to efficiently navigate complex codebases when identifying relevant code sections. The challenge lies in bridging natural language problem descriptions with the appropriate code elements, often requiring reasoning across hierarchical structures and multiple dependencies. We introduce LocAgent, a framework that addresses ...
  - **Labels**: [agent design](agent_design.md), [prompt strategy](prompt_strategy.md), [retrieval-augmented generation](retrieval-augmented_generation.md), [planning](planning.md)


- [Repairagent: An autonomous, llm-based agent for program repair](../venues/arXiv2024/paper_11.md), ([arXiv2024](../venues/arXiv2024/README.md))

  - **Abstract**: Automated program repair has emerged as a powerful technique to mitigate the impact of software bugs on system reliability and user experience. This paper introduces RepairAgent, the first work to address the program repair challenge through an autonomous agent based on a large language model (LLM). Unlike existing deep learning-based approaches, which prompt a model with a fixed prompt or in a fixed feedback loop, our work treats the LLM as an agent capable of autonomously planning and executin...
  - **Labels**: [code generation](code_generation.md), [program repair](program_repair.md), [agent design](agent_design.md), [planning](planning.md)


- [RepoAudit: An Autonomous LLM-Agent for Repository-Level Code Auditing](../venues/ICML2025/paper_2.md), ([ICML2025](../venues/ICML2025/README.md))

  - **Abstract**: Code auditing is a code review process with the goal of finding bugs. Large Language Models (LLMs) have shown substantial potential in this task, offering the ability to analyze programs without compilation and enabling customized bug detection following specified prompts. However, applying LLMs to repository-level code auditing presents notable challenges. The inherent context limits and hallucinations of LLMs can lead to the low quality of bug reports. Meanwhile, the large size of software rep...
  - **Labels**: [static analysis](static_analysis.md), [bug detection](bug_detection.md), [agent design](agent_design.md), [prompt strategy](prompt_strategy.md), [retrieval-augmented generation](retrieval-augmented_generation.md), [planning](planning.md)


- [RepoGraph: Enhancing AI Software Engineering with Repository-level Code Graph](../venues/ICLR2025/paper_4.md), ([ICLR2025](../venues/ICLR2025/README.md))

  - **Abstract**: Large Language Models (LLMs) excel in code generation yet struggle with modern AI software engineering tasks. Unlike traditional function-level or file-level coding tasks, AI software engineering requires not only basic coding proficiency but also advanced skills in managing and interacting with code repositories. However, existing methods often overlook the need for repository-level code understanding, which is crucial for accurately grasping the broader context and developing effective solutio...
  - **Labels**: [agent design](agent_design.md), [prompt strategy](prompt_strategy.md), [retrieval-augmented generation](retrieval-augmented_generation.md), [planning](planning.md)


- [Self-Planning Code Generation with Large Language Models](../venues/TOSEM2024/paper_2.md), ([TOSEM2024](../venues/TOSEM2024/README.md))

  - **Abstract**: Although large language models (LLMs) have demonstrated impressive ability in code generation, they are still struggling to address the complicated intent provided by humans. It is widely acknowledged that humans typically employ planning to decompose complex problems and schedule solution steps prior to implementation. To this end, we introduce planning into code generation to help the model understand complex intent and reduce the difficulty of problem-solving. This paper proposes a self-plann...
  - **Labels**: [code generation](code_generation.md), [program synthesis](program_synthesis.md), [agent design](agent_design.md), [planning](planning.md), [empirical study](empirical_study.md)


- [Symbolic Planning and Code Generation for Grounded Dialogue](../venues/EMNLP2023/paper_4.md), ([EMNLP2023](../venues/EMNLP2023/README.md))

  - **Abstract**: Large language models (LLMs) excel at processing and generating text and code. However, LLMs have had limited applicability in grounded task-oriented dialogue as they are difficult to steer toward task objectives and fail to handle novel grounding. We present a modular and interpretable grounded dialogue system that addresses these shortcomings by composing LLMs with a symbolic planner and grounded code execution. Our system, consists of a reader and planner: the reader leverages an LLM to conve...
  - **Labels**: [code generation](code_generation.md), [program synthesis](program_synthesis.md), [agent design](agent_design.md), [planning](planning.md)


- [Unleashing the Emergent Cognitive Synergy in Large Language Models: A Task-Solving Agent through Multi-Persona Self-Collaboration](../venues/NAACL2024/paper_1.md), ([NAACL2024](../venues/NAACL2024/README.md))

  - **Abstract**: Human intelligence thrives on cognitive synergy, where collaboration among different minds yield superior outcomes compared to isolated individuals. In this work, we propose Solo Performance Prompting (SPP), which transforms a single LLM into a cognitive synergist by engaging in multi-turn self-collaboration with multiple personas. A cognitive synergist is an intelligent agent that collaboratively combines multiple minds’ strengths and knowledge to enhance problem-solving in complex tasks. By dy...
  - **Labels**: [agent design](agent_design.md), [planning](planning.md)


- [{C}ode{T}ree: Agent-guided Tree Search for Code Generation with Large Language Models](../venues/NAACL2025/paper_5.md), ([NAACL2025](../venues/NAACL2025/README.md))

  - **Abstract**: Pretrained on massive amounts of code and text data, large language models (LLMs) have demonstrated remarkable achievements in performing code generation tasks. With additional execution-based feedback, these models can act as agents with capabilities to self-refine and improve generated code autonomously. However, on challenging coding tasks with extremely large search space, current agentic approaches still struggle with multi-stage planning, generating, and debugging. To address this problem,...
  - **Labels**: [code generation](code_generation.md), [program synthesis](program_synthesis.md), [agent design](agent_design.md), [planning](planning.md)
