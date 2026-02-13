# LLM Story Point Estimation

This repository contains the data and code for the paper "Story Point Estimation with LLMs".

## Repository Structure (New)

The repository has been restructured to align with the research questions (RQ1-RQ4) from the paper.

### Data Organization

The `results/` directory is now organized by Research Question and technique:

*   **RQ1: Zero-Shot Direct Prediction**
    *   `results/RQ1_ZeroShot_Direct/{model}/`
*   **RQ2: Few-Shot Direct Prediction**
    *   `results/RQ2_FewShot_Direct/{model}/`
    *   *Note:* DeepSeek has `standard` and `scale_aware` subdirectories. OpenAI has `file_based` and `common_examples`.
*   **RQ3: Zero-Shot Comparative**
    *   `results/RQ3_ZeroShot_Comparative/{model}/`
*   **RQ4: Few-Shot Comparative**
    *   `results/RQ4_FewShot_Comparative/{model}/`

### Models

*   Gemini
*   OpenAI (GPT-4o/3.5)
*   Kimi (Moonshot)
*   DeepSeek

## Data Migration Mapping

| Old Path | New Path | Description |
| :--- | :--- | :--- |
| `results/zero_shot/basic_prompt_gemini*` | `results/RQ1_ZeroShot_Direct/gemini/` | Gemini Zero-Shot Direct |
| `results/zero_shot/basic_prompt_openai*` | `results/RQ1_ZeroShot_Direct/openai/` | OpenAI Zero-Shot Direct |
| `results/zero_shot/kimi_k2_raw/` | `results/RQ1_ZeroShot_Direct/kimi/` | Kimi Zero-Shot Direct |
| `results/12.09_mx/result/*zeroshot*` | `results/RQ1_ZeroShot_Direct/deepseek/` | DeepSeek Zero-Shot Direct |
| `results/few_shot/Basic common examples/gemini*` | `results/RQ2_FewShot_Direct/gemini/` | Gemini Few-Shot Direct |
| `results/few_shot/Basic File based examples/openai*` | `results/RQ2_FewShot_Direct/openai/file_based/` | OpenAI Few-Shot Direct (File) |
| `results/few_shot/Basic common examples/openai*` | `results/RQ2_FewShot_Direct/openai/common_examples/` | OpenAI Few-Shot Direct (Common) |
| `results/few_shot/kimik2/new_sb-few_shot-scaleAware` | `results/RQ2_FewShot_Direct/kimi/scale_aware/` | Kimi Few-Shot Scale Aware |
| `results/12.09_mx/result/*fewshot*` | `results/RQ2_FewShot_Direct/deepseek/standard/` | DeepSeek Few-Shot Direct |
| `results/12.09_mx/result/*scaleAware*` | `results/RQ2_FewShot_Direct/deepseek/scale_aware/` | DeepSeek Scale Aware |
| `results/gemini pairwise with accuracy/` | `results/RQ3_ZeroShot_Comparative/gemini/` | Gemini Zero-Shot Comparative |
| `results/Pairwise_zero_shot/pairwise__12.16_mx/pairwise_zeroshot` | `results/RQ3_ZeroShot_Comparative/deepseek/` | DeepSeek Zero-Shot Comparative |
| `results/Pairwise_zero_shot/pairwise_Pranam` | `results/RQ3_ZeroShot_Comparative/kimi/` | Kimi Zero-Shot Comparative |
| `results/Prompt 4/gemini/` | `results/RQ4_FewShot_Comparative/gemini/` | Gemini Few-Shot Comparative |
| `results/prompt4_02.03_mx/` | `results/RQ4_FewShot_Comparative/deepseek/` | DeepSeek Few-Shot Comparative |
| `results/fewshot_pairwise_direct_ps/` | `results/RQ4_FewShot_Comparative/kimi/` | Kimi Few-Shot Comparative |

## Original Data

The original datasets remain in the `data/` directory.
