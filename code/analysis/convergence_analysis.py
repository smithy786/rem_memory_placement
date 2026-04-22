#CONVERGENCE#

import pandas as pd
import re

df = pd.read_csv("data/rem_experiment_results.csv")

def convergence(text, rem_str):
    tokens = re.findall(r'\b\w+\b', rem_str.lower())
    if not tokens:
        return 0
    text = str(text).lower()
    return sum(t in text for t in tokens) / len(tokens)

results = []

for _, row in df.iterrows():
    results.append({
        "pre": convergence(row["pre_response"], row["rems"]),
        "post": convergence(row["post_response"], row["rems"])
    })

out = pd.DataFrame(results)
print("PRE:", out["pre"].mean())
print("POST:", out["post"].mean())