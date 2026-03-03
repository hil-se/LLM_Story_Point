# Story Point Estimation with LLMs

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

This repository contains the replication package, datasets, and analysis scripts for the research paper: **"Story Point Estimation with LLMs"**.

In this study, we empirically evaluate the capabilities of four leading Large Language Models (LLMs) in automating story point estimation across 16 real-world agile software projects. We investigate their performance across four different prompting setups: zero-shot direct estimation, few-shot direct estimation, zero-shot comparative estimation, and few-shot comparative estimation.

## Models Evaluated

Our evaluation includes four state-of-the-art models accessed via their respective APIs:
- **DeepSeek-R1** (`deepseek-reasoner`): An advanced reasoning model utilizing reinforcement learning and a Mixture-of-Experts architecture.
- **Kimi / Moonshot K2** (`moonshotai/kimi-k2-instruct-0905`): A model renowned for rigorous instruction-following and long-context capabilities.
- **OpenAI** (`gpt-5-nano`): A highly efficient model designed for rapid interaction and extensive context processing.
- **Gemini Flash Lite** (`gemini-2.5-flash-lite`): A lightweight model built for high-speed inference with a massive context window.

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
    ├── RQ3_ZeroShot_Comparative/
    └── RQ4_FewShot_Comparative/
```

## Experimental Results & Data Formats

The experimental outputs are cleanly partitioned into four directories corresponding to the evaluation strategies. Inside each directory, results are grouped by the model. 

### RQ1: Zero-Shot Direct Prediction
Evaluating the LLMs' inherent zero-shot capability to predict functional story points.
- **Path:** `results/RQ1_ZeroShot_Direct/<model>/`
- **Format:** `*_<model>_ZeroShot.csv`

### RQ2: Few-Shot Direct Prediction
Evaluating the impact of providing historical, labeled story point examples in the prompt to calibrate the model's absolute scale. Experiments evaluated "Count" (most frequent) and "Scale" (scale-aware) few-shot selection.
- **Path:** `results/RQ2_FewShot_Direct/<model>/Count/` and `results/RQ2_FewShot_Direct/<model>/Scale/`
- **Format:** `*_<model>_Count.csv` and `*_<model>_Scale.csv`

### RQ3: Zero-Shot Comparative
Asking the model to explicitly compare the relative effort between two backlog items (predicting if one is strictly greater, less than, or equal to the other).
- **Path:** `results/RQ3_ZeroShot_Comparative/<model>/`
- **Format:** `*_<model>_ZeroShotComparative.csv`

### RQ4: Few-Shot Comparative
Providing relative comparison examples in the prompt before asking the LLM to output absolute story point predictions for new items.
- **Path:** `results/RQ4_FewShot_Comparative/<model>/`
- **Format:** `*_<model>_FewShotComparative.csv`

> **Note:** For every model inside these directories, an `evaluate_*.csv` summary file exists (e.g., `evaluate_ZeroShot.csv`, `evaluate_Count.csv`), containing aggregated performance metrics like Pearson (ρ) and Spearman (r_s) correlations.

## License
This project is licensed under the MIT License - see the LICENSE file for details.
