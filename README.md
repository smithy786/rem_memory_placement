

# Recursive Embedded Memories (REMs):  
## Memory Placement and Integrative Behaviour in Language Models



📄 **Paper (Full PDF):**  
👉 **[Download here](paper/paper.pdf)**

This repository contains the code and experimental pipeline for **Paper 2** in the REMs series.

## Overview

This work investigates how the placement of **Recursive Embedded Memories (REMs)** affects the behaviour of Large Language Models (LLMs).

We compare three conditions:

- **Control** — no memory provided  
- **Pre-Load (PRE)** — REMs placed before the user input  
- **Post-Load (POST)** — REMs placed after the user input  

The goal is to determine whether memory acts as:

- **directive context** (PRE), or  
- **integrated internal state** (POST)

---

## Key Finding

Memory placement is not neutral.

- Logic tasks → minimal effect  
- Ethics tasks → moderate effect  
- Abstract tasks → strong effect  

In abstract prompts, POST placement produces:

- **+18.3% convergence lift**
- **69.7% win rate over PRE**

This transition is referred to as the **“Abstract Leap”**.

---

## Repository Structure

```bash

.
├── code
│ ├── analysis
│ │ ├── analyze_results.py
│ │ ├── convergence_analysis.py
│ │ └── plot_results.py
│ └── pipeline
│ └── rem_experiment.py
├── data
│ ├── README.md
│ └── test_inputs.py
├── figures
│ └── README.md
├── notes
│ └── README.md
├── paper
│ ├── paper.tex
│ └── pre_post_load.pdf
└── README.md

---


## Running the Experiment

### 1. Generate responses

python3 code/pipeline/rem_experiment.py

This will:

retrieve REMs
generate CONTROL / PRE / POST outputs
save results to:

data/rem_experiment_results.csv

2. Analyze semantic alignment

python3 code/analysis/analyze_results.py

Outputs:

REM similarity
PRE / POST lift

3. Analyze convergence

python3 code/analysis/convergence_analysis.py

Outputs:

token-level REM integration

4. Generate figures

python3 code/analysis/plot_results.py

Data

All experiments use:

data/test_inputs.py
Prompt set (Logic / Ethics / Abstract)
rem_entries.jsonl
rem_embeddings.npy

These must be present locally.

Notes
All conditions are run independently
No shared state between CONTROL / PRE / POST
Embedding model: BAAI/bge-small-en

Relation to Paper 1

This work builds on:

Recursive Embedded Memories (REMs):
A Trigrammatic Compression Protocol for High-Density Semantic Representation

Paper 1 introduces:

REM encoding
compression pipeline
semantic retention

Paper 2 focuses on:

memory placement
behavioural effect
integration vs directive use

Summary

This repository isolates a single variable:

Where memory is placed

and shows that this alone changes how a model behaves.

Author

William Leyshon
SmithWork-AI, United Kingdom