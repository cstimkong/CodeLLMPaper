# Mystique: Automated Vulnerability Patch Porting with Semantic and Syntactic-Enhanced LLM

**Authors**: Wu, Susheng and Wang, Ruisi and Cao, Yiheng and Chen, Bihuan and Zhou, Zhuotong and Huang, Yiheng and Zhao, JunPeng and Peng, Xin

**Abstract**:

Branching repositories facilitates efficient software development but can also inadvertently propagate vulnerabilities. When an original branch is patched, other unfixed branches remain vulnerable unless the patch is successfully ported. However, due to inherent discrepancies between branches, many patches cannot be directly applied and require manual intervention, which is time-consuming and leads to delays in patch porting, increasing vulnerability risks. Existing automated patch porting approaches are prone to errors, as they often overlook essential semantic and syntactic context of vulnerability and fail to detect or refine faulty patches.        We propose Mystique, a novel LLM-based approach to address these limitations. Mystique first slices the semantic-related statements linked to the vulnerability while ensuring syntactic correctness, allowing it to extract the signatures for both the original patched function and the target vulnerable function. Mystique then utilizes a fine-tuned LLM to generate a fixed function, which is further iteratively checked and refined to ensure successful porting. Our evaluation shows that Mystique achieved a success rate of 0.954 at function level and of 0.924 at CVE level, outperforming state-of-the-art approaches by at least 13.2\% at function level and 12.3\% at CVE level. Our evaluation also demonstrates Mystique’s superior generality across various projects, bugs, and programming languages. Mystique successfully ported patches for 34 real-world vulnerable branches.

**Link**: [Read Paper](https://doi.org/10.1145/3715718)

**Labels**: [code generation](../../labels/code_generation.md), [program repair](../../labels/program_repair.md)
