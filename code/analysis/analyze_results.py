
#semantic lift#

import pandas as pd
import numpy as np
from sentence_transformers import SentenceTransformer

df = pd.read_csv("data/rem_experiment_results.csv")

embed_model = SentenceTransformer("BAAI/bge-small-en")

def parse_rems(rem_string):
    if pd.isna(rem_string):
        return []
    return [r.strip() for r in rem_string.split("\n") if r.strip()]

def similarity(text, rems):
    if not rems:
        return 0
    tvec = embed_model.encode([text], normalize_embeddings=True)[0]
    rvecs = embed_model.encode(rems, normalize_embeddings=True)
    return np.mean([np.dot(tvec, r) for r in rvecs])

results = []

for _, row in df.iterrows():
    rems = parse_rems(row["rems"])

    control = similarity(row["control_response"], rems)
    pre = similarity(row["pre_response"], rems)
    post = similarity(row["post_response"], rems)

    results.append({
        "control": control,
        "pre": pre,
        "post": post,
        "pre_lift": pre - control,
        "post_lift": post - control
    })

out = pd.DataFrame(results)
out.to_csv("data/rem_analysis_results.csv", index=False)

print(out.mean())