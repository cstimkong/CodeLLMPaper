# NDSS2025

Number of papers: 8

## [Beyond Classification: Inferring Function Names in Stripped Binaries via Domain Adapted LLMs](paper_4.md)
- **Authors**: Linxi Jiang and Xin Jin and Zhiqiang Lin
- **Abstract**: Function name inference in stripped binaries is an important yet challenging task for many security applications, such as malware analysis and vulnerability discovery, due to the need to grasp binary code semantics amidst diverse instruction sets, architectures, compiler optimizations, and obfuscations. While machine learning has made significant progress in this field, existing methods often struggle with unseen data, constrained by their reliance on a limited vocabulary-based classification ap...
- **Link**: [Read Paper](https://www.ndss-symposium.org/ndss-paper/beyond-classification-inferring-function-names-in-stripped-binaries-via-domain-adapted-llms)
- **Labels**: [code model](../../labels/code_model.md), [code model training](../../labels/code_model_training.md), [binary code model](../../labels/binary_code_model.md), [static analysis](../../labels/static_analysis.md), [program decompilation](../../labels/program_decompilation.md)


## [EAGLEYE: Exposing Hidden Web Interfaces in IoT Devices via Routing Analysis](paper_5.md)
- **Authors**: Hangtian Liu and Lei Zheng and Tsinghua University) and Shuitao Gan and Chao Zhang and Tsinghua University) and Zicong Gao and Hongqi Zhang and Yishun Zeng and Tsinghua University) and Zhiyuan Jiang and Jiahai Yang and Tsinghua University)
- **Abstract**: Hidden web interfaces, i.e., undisclosed access channels in IoT devices, introduce great security risks and have resulted in severe attacks in recent years. However, the definition of such threats is vague, and few solutions are able to discover them. Due to their hidden nature, traditional bug detection solutions (e.g., taint analysis, fuzzing) are hard to detect them. In this paper, we present a novel solution EAGLEYE to automatically expose hidden web interfaces in IoT devices. By analyzing i...
- **Link**: [Read Paper](https://www.ndss-symposium.org/ndss-paper/eagleye-exposing-hidden-web-interfaces-in-iot-devices-via-routing-analysis)
- **Labels**: [static analysis](../../labels/static_analysis.md), [bug detection](../../labels/bug_detection.md), [specification inference](../../labels/specification_inference.md)


## [Enhancing Security in Third-Party Library Reuse – Comprehensive Detection of 1-day Vulnerability through Code Patch Analysis](paper_6.md)
- **Authors**: Shangzhi Xu and Jialiang Dong and Weiting Cai and Juanru Li and Arash Shaghaghi and Nan Sun and Siqi Ma
- **Abstract**: Nowadays, software development progressesrapidly to incorporate new features. To facilitate such growthand provide convenience for developers when creating andupdating software, reusing open-source software (i.e., thirdpartylibrary reuses) has become one of the most effectiveand efficient methods. Unfortunately, the practice of reusingthird-party libraries (TPLs) can also introduce vulnerabilities(known as 1-day vulnerabilities) because of the low maintenanceof TPLs, resulting in many vulnerable...
- **Link**: [Read Paper](https://www.ndss-symposium.org/ndss-paper/enhancing-security-in-third-party-library-reuse-comprehensive-detection-of-1-day-vulnerability-through-code-patch-analysis)
- **Labels**: [static analysis](../../labels/static_analysis.md), [bug detection](../../labels/bug_detection.md), [specification inference](../../labels/specification_inference.md)


## [From Large to Mammoth: A Comparative Evaluation of Large Language Models in Vulnerability Detection](paper_7.md)
- **Authors**: Jie Lin and David Mohaisen
- **Abstract**: Large Language Models (LLMs) have demonstrated strong potential in tasks such as code understanding and generation. This study evaluates several advanced LLMs—such as LLaMA-2, CodeLLaMA, LLaMA-3, Mistral, Mixtral, Gemma, CodeGemma, Phi-2, Phi-3, and GPT-4—for vulnerability detection, primarily in Java, with additional tests in C/C++ to assess generalization. We transition from basic positive sample detection to a more challenging task involving both positive and negative samples and evaluate the...
- **Link**: [Read Paper](https://www.ndss-symposium.org/ndss-paper/from-large-to-mammoth-a-comparative-evaluation-of-large-language-models-in-vulnerability-detection)
- **Labels**: [static analysis](../../labels/static_analysis.md), [bug detection](../../labels/bug_detection.md), [empirical study](../../labels/empirical_study.md)


## [Generating API Parameter Security Rules with LLM for API Misuse Detection](paper_1.md)
- **Authors**: Jinghua Liu and Chinese Academy of Sciences and Beijing and China; School of Cyber Security and University of Chinese Academy of Sciences and China) and Yi Yang and Chinese Academy of Sciences and Beijing and China; School of Cyber Security and University of Chinese Academy of Sciences and China) and Kai Chen and Chinese Academy of Sciences and Beijing and China; School of Cyber Security and University of Chinese Academy of Sciences and China) and Miaoqian Lin and Chinese Academy of Sciences and Beijing and China; School of Cyber Security and University of Chinese Academy of Sciences and China)
- **Abstract**: When utilizing library APIs, developers should follow the API security rules to mitigate the risk of API misuse. API Parameter Security Rule (APSR) is a common type of security rule that specifies how API parameters should be safely used and places constraints on their values. Failure to comply with the APSRs can lead to severe security issues, including null pointer dereference and memory corruption. Manually analyzing numerous APIs and their parameters to construct APSRs is labor-intensive and...
- **Link**: [Read Paper](https://www.ndss-symposium.org/ndss-paper/generating-api-parameter-security-rules-with-llm-for-api-misuse-detection)
- **Labels**: [static analysis](../../labels/static_analysis.md), [bug detection](../../labels/bug_detection.md), [specification inference](../../labels/specification_inference.md)


## [PropertyGPT: LLM-driven Formal Verification of Smart Contracts through Retrieval-Augmented Property Generation](paper_8.md)
- **Authors**: Ye Liu and Yue Xue and Daoyuan Wu and Yuqiang Sun and Yi Li and Miaolei Shi and Yang Liu
- **Abstract**: Formal verification is a technique that can prove the correctness of a system with respect to a certain specification or property. It is especially valuable for security-sensitive smart contracts that manage billions in cryptocurrency assets. Although existing research has developed various static verification tools (or provers) for smart contracts, a key missing component is theautomated generation of comprehensive properties, including invariants, pre-/post-conditions, and rules. Hence, indust...
- **Link**: [Read Paper](https://www.ndss-symposium.org/ndss-paper/propertygpt-llm-driven-formal-verification-of-smart-contracts-through-retrieval-augmented-property-generation)
- **Labels**: [static analysis](../../labels/static_analysis.md), [bug detection](../../labels/bug_detection.md), [program verification](../../labels/program_verification.md)


## [RACONTEUR: A Knowledgeable, Insightful, and Portable LLM-Powered Shell Command Explainer](paper_2.md)
- **Authors**: Jiangyi Deng and Xinfeng Li and Yanjiao Chen and Yijie Bai and Haiqin Weng and Yan Liu and Tao Wei and Wenyuan Xu
- **Abstract**: Malicious shell commands are linchpins to many cyber-attacks, but may not be easy to understand by security analysts due to complicated and often disguised code structures. Advances in large language models (LLMs) have unlocked the possibility of generating understandable explanations for shell commands. However, existing general-purpose LLMs suffer from a lack of expert knowledge and a tendency to hallucinate in the task of shell command explanation. In this paper, we present Raconteur, a knowl...
- **Link**: [Read Paper](https://www.ndss-symposium.org/ndss-paper/raconteur-a-knowledgeable-insightful-and-portable-llm-powered-shell-command-explainer)
- **Labels**: [static analysis](../../labels/static_analysis.md), [code summarization](../../labels/code_summarization.md), [agent design](../../labels/agent_design.md), [prompt strategy](../../labels/prompt_strategy.md), [retrieval-augmented generation](../../labels/retrieval-augmented_generation.md)


## [The Midas Touch: Triggering the Capability of LLMs for RM-API Misuse Detection](paper_3.md)
- **Authors**: Yi Yang and Chinese Academy of Sciences and Beijing and China; School of Cyber Security and University of Chinese Academy of Sciences and China) and Jinghua Liu and Chinese Academy of Sciences and Beijing and China; School of Cyber Security and University of Chinese Academy of Sciences and China) and Kai Chen and Chinese Academy of Sciences and Beijing and China; School of Cyber Security and University of Chinese Academy of Sciences and China) and Miaoqian Lin and Chinese Academy of Sciences and Beijing and China; School of Cyber Security and University of Chinese Academy of Sciences and China)
- **Abstract**: As the basis of software resource management (RM), strictly following the RM-API constraints guarantees secure resource management and software. To enhance the RM-API application, researchers find it effective in detecting RM-API misuse on open-source software according to RM-API constraints retrieved from documentation and code. However, the current pattern-matching constraint retrieval methods have limitations: the documentation-based methods leave many API constraints irregularly distributed ...
- **Link**: [Read Paper](https://www.ndss-symposium.org/ndss-paper/the-midas-touch-triggering-the-capability-of-llms-for-rm-api-misuse-detection)
- **Labels**: [static analysis](../../labels/static_analysis.md), [bug detection](../../labels/bug_detection.md), [specification inference](../../labels/specification_inference.md)
