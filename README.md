# Story Point Estimation with LLMs

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

This repository contains the replication package, datasets, and analysis scripts for the research paper: **"Story Point Estimation with LLMs"**.

In this study, we empirically evaluate the capabilities of four leading Large Language Models (LLMs) in automating story point estimation across 16 real-world agile software projects. We investigate their performance across four different prompting setups: zero-shot direct estimation, few-shot direct estimation, zero-shot comparative estimation, and few-shot comparative estimation.

## Models Evaluated

Our evaluation includes four state-of-the-art models (2 open-source and 2 closed-source) accessed via their respective APIs:
- **DeepSeek-V3.2** (`deepseek-v4-flash`): An open-source, high‑reasoning Transformer model with a sparse Mixture‑of‑Experts architecture.
- **Qwen 3 32B** (`qwen-3-32b`): An open-source, highly capable 32-billion parameter instruction-tuned model.
- **OpenAI** (`gpt-5-nano`): A closed-source, highly efficient model designed for rapid interaction and extensive context processing.
- **Gemini Flash Lite** (`gemini-2.5-flash-lite`): A closed-source, lightweight model built for high-speed inference with a massive context window.

## Repository Structure

The repository is organized to map directly to the four Research Questions (RQs) posed in the paper. 

```text
LLM_Story_Point/
├── README.md                           # This file
├── Story_point_estimation_with_LLMs/   # LaTeX source code for the research paper
├── data/                               # Original raw project datasets
│   ├── few_shot_samples/               # Pre-selected few-shot examples
│   ├── test/                           # True test datasets
└── results/                            # Main experimental results
    ├── RQ1_ZeroShot_Direct/
    ├── RQ2_FewShot_Direct/
    │   └── qwen/
    │       ├── count/                  # Frequency-based few-shot results
    │       └── scale/                  # Scale-aware few-shot results
    ├── RQ3_ZeroShot_Comparative/
    ├── RQ4_FewShot_Comparative/
    └── evaluation_qwen/                # Structured evaluation metrics and summaries for Qwen
        ├── project_pearson_spearman.csv   # Per-run metrics and runtime stats
        ├── evaluation_project_summary.csv # Mean/std summary for each project
        └── evaluation_overall_summary.csv # Overall paper-ready summary metrics
```

## Experimental Results & Data Formats

The experimental outputs are cleanly partitioned into four directories corresponding to the evaluation strategies. Inside each directory, results are grouped by the model.

### RQ1: Zero-Shot Direct Prediction
Evaluating the LLMs' inherent zero-shot capability to predict functional story points.
- **Path:** `results/RQ1_ZeroShot_Direct/<model>/`
- **Format:** `*_<model>_ZeroShot.csv`

### RQ2: Few-Shot Direct Prediction
Evaluating the impact of providing historical, labeled story point examples in the prompt to calibrate the model's absolute scale. Experiments evaluated "Count" (most frequent) and "Scale" (scale-aware) few-shot selection.
- **Path:** `results/RQ2_FewShot_Direct/<model>/count/` and `results/RQ2_FewShot_Direct/<model>/scale/`
- **Format:** `*_<model>_FewShot.csv` and `*_<model>_FewShot_Scale.csv`

### RQ3: Zero-Shot Comparative
Asking the model to explicitly compare the relative effort between two backlog items (predicting if one is strictly greater, less than, or equal to the other).
- **Path:** `results/RQ3_ZeroShot_Comparative/<model>/`
- **Format:** `*_<model>_RQ3_ZeroShot_Comparative.csv`

### RQ4: Few-Shot Comparative
Providing relative comparison examples in the prompt before asking the LLM to output absolute story point predictions for new items.
- **Path:** `results/RQ4_FewShot_Comparative/<model>/`
- **Format:** `*_<model>_RQ4_FewShot_Comparative.csv`

> **Note:** Performance summaries for each model are tracked via automated scripts to produce clean statistical correlation matrices (Pearson ρ, Spearman r_s) and error indicators (MAE, RMSE, Accuracy).

## License
This project is licensed under the MIT License - see the LICENSE file for details.
