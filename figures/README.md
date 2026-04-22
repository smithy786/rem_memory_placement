# Figures

This directory contains plots generated from the analysis scripts.

Examples include:
- REM Lift comparisons
- Convergence comparisons
- Cross-domain summaries

### REM Architecture Performance Data

| Domain | Configuration | REM Lift (Mean) | Convergence Score |
| :--- | :--- | :--- | :--- |
| **Logic** | Pre-Load | -0.00012 | 0.2302 |
| **Logic** | Post-Load | +0.00210 | 0.3060 |
| **Ethics** | Pre-Load | +0.00687 | 0.4460 |
| **Ethics** | Post-Load | +0.00802 | 0.4958 |
| **Abstract** | Post-Load | -0.00382 | 0.3916 |
| **Abstract** | Post-Load | +0.00180 | 0.5745 |



### Statistical Key Findings (The "Abstract Leap")

    Convergence Lift (ΔC):

        Logic: +0.0757

        Ethics: +0.0498

        Abstract: +0.1829 (The peak internal synthesis threshold)

    POST > PRE Win Rate (Convergence):

        Logic: 39.4%

        Ethics: 48.5%

        Abstract: 69.7%


Figures are generated using:
code/analysis/plot_results.py

