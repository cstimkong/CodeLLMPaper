# MLLM-Based UI2Code Automation Guided by UI Layout Information

**Authors**: Wu, Fan and Gao, Cuiyun and Li, Shuqing and Wen, Xin-Cheng and Liao, Qing

**Abstract**:

Converting user interfaces into code (UI2Code) is a crucial step in website development, which is time-consuming and labor-intensive. The automation of UI2Code is essential to streamline this task, beneficial for improving the development efficiency. There exist deep learning-based methods for the task; however, they heavily rely on a large amount of labeled training data and struggle with generalizing to real-world, unseen web page designs. The advent of Multimodal Large Language Models (MLLMs) presents potential for alleviating the issue, but they are difficult to comprehend the complex layouts in UIs and generate the accurate code with layout preserved. To address these issues, we propose LayoutCoder, a novel MLLM-based framework generating UI code from real-world webpage images, which includes three key modules: (1) Element Relation Construction, which aims at capturing UI layout by identifying and grouping components with similar structures; (2) UI Layout Parsing, which aims at generating UI layout trees for guiding the subsequent code generation process; and (3) Layout-Guided Code Fusion, which aims at producing the accurate code with layout preserved. For evaluation, we build a new benchmark dataset which involves 350 real-world websites named Snap2Code, divided into seen and unseen parts for mitigating the data leakage issue, besides the popular dataset Design2Code. Extensive evaluation shows the superior performance of LayoutCoder over the state-of-the-art approaches. Compared with the best-performing baseline, LayoutCoder improves 10.14\% in the BLEU score and 3.95\% in the CLIP score on average across all datasets.

**Link**: [Read Paper](https://doi.org/10.1145/3728925)

**Labels**: [code generation](../../labels/code_generation.md), [program synthesis](../../labels/program_synthesis.md)
