# Divide-and-Conquer: Generating UI Code from Screenshots

**Authors**: Wan, Yuxuan and Wang, Chaozheng and Dong, Yi and Wang, Wenxuan and Li, Shuqing and Huo, Yintong and Lyu, Michael

**Abstract**:

Websites are critical in today’s digital world, with over 1.11 billion currently active and approximately 252,000 new sites launched daily. Converting website layout design into functional UI code is a time-consuming yet indispensable step of website development. Manual methods of converting visual designs into functional code present significant challenges, especially for non-experts. To explore automatic design-to-code solutions, we first conduct a motivating study on GPT-4o and identify three types of issues in generating UI code: element omission, element distortion, and element misarrangement. We further reveal that a focus on smaller visual segments can help multimodal large language models (MLLMs) mitigate these failures in the generation process. In this paper, we propose DCGen, a divide-and-conquer-based approach to automate the translation of webpage design to UI code. DCGen starts by dividing screenshots into manageable segments, generating code for each segment, and then reassembling them into complete UI code for the entire screenshot. We conduct extensive testing with a dataset comprised of real-world websites and various MLLMs and demonstrate that DCGen achieves up to a 15\% improvement in visual similarity and 8\% in code similarity for large input images. Human evaluations show that DCGen can help developers implement webpages significantly faster and more similar to the UI designs. To the best of our knowledge, DCGen is the first segment-aware MLLM-based approach for generating UI code directly from screenshots.

**Link**: [Read Paper](https://doi.org/10.1145/3729364)

**Labels**: [code generation](../../labels/code_generation.md), [program synthesis](../../labels/program_synthesis.md)
