#PLOTTING#

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/rem_analysis_results.csv")

plt.figure()
plt.bar(["PRE", "POST"], [df["pre_lift"].mean(), df["post_lift"].mean()])
plt.title("REM Lift")
plt.savefig("figures/lift.png")

print("Saved.")