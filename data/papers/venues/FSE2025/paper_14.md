# LLMDroid: Enhancing Automated Mobile App GUI Testing Coverage with Large Language Model Guidance

**Authors**: Wang, Chenxu and Liu, Tianming and Zhao, Yanjie and Yang, Minghui and Wang, Haoyu

**Abstract**:

With the rapid development of Large Language Models (LLMs), their integration into automated mobile GUI testing has emerged as a promising research direction. However, existing LLM-based testing approaches face significant challenges, including time inefficiency and high costs due to constant LLM querying. To address these issues, this paper introduces LLMDroid, a novel testing framework designed to enhance existing automated mobile GUI testing tools by leveraging LLMs more efficiently. The workflow of LLMDroid comprises two main stages: Autonomous Exploration and LLM Guidance. During Autonomous Exploration, LLMDroid utilizes existing testing tools while leveraging LLMs to summarize explored pages. When code coverage growth slows, it transitions to LLM Guidance to strategically direct testing towards unexplored functionalities. This approach minimizes LLM interactions while maximizing their impact on test coverage. We applied LLMDroid to three popular open-source Android testing tools and evaluated it on 14 top-listed apps from Google Play. Results demonstrate an average increase of 26.16\% in code coverage and 29.31\% in activity coverage. Furthermore, our evaluation under different LLMs reveals that LLMDroid outperform existing step-wise approaches with significant cost efficiency, achieving optimal performance at $0.49 per hour using GPT-4o among tested models, with a cost-effective alternative achieving 94\% of this performance at just $0.03 per hour. These findings highlight LLMDroid’s effectiveness in enhancing automated mobile app testing and its potential for widespread adoption.

**Link**: [Read Paper](https://doi.org/10.1145/3715763)

**Labels**: [program testing](../../labels/program_testing.md), [GUI testing](../../labels/GUI_testing.md)
