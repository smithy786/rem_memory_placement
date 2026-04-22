import json
import numpy as np
import pandas as pd
from sentence_transformers import SentenceTransformer
from model_client import ModelClient
from data.test_inputs import test_inputs

client = ModelClient()

REM_ENTRIES_FILE = "rem_entries.jsonl"
REM_EMB_FILE = "rem_embeddings.npy"

# Load DB
emb = np.load(REM_EMB_FILE)

entries = []
with open(REM_ENTRIES_FILE) as f:
    for line in f:
        entries.append(json.loads(line))

model = SentenceTransformer("BAAI/bge-small-en")

def retrieve_rems(query, top_k=5):
    qvec = model.encode([query], normalize_embeddings=True)[0]
    scores = emb @ qvec
    idx = np.argsort(scores)[-top_k:][::-1]
    return [f"{entries[i]['node']} → {entries[i]['payload']}" for i in idx]

def build_control(user_input):
    return f"User input:\n{user_input}"

def build_pre(user_input, rems):
    return f"""
Internal mental state:
{chr(10).join(rems)}

User input:
{user_input}
"""

def build_post(user_input, rems):
    return f"""
User input:
{user_input}

Internal mental state:
{chr(10).join(rems)}
"""

results = []

for i, user_input in enumerate(test_inputs, 1):

    rems = retrieve_rems(user_input)

    control = client.generate("Respond naturally.", build_control(user_input))
    pre = client.generate("Use internal context.", build_pre(user_input, rems))
    post = client.generate("Integrate internal state.", build_post(user_input, rems))

    results.append({
        "input": user_input,
        "rems": "\n".join(rems),
        "control_response": control,
        "pre_response": pre,
        "post_response": post
    })

    print(f"Completed {i}/{len(test_inputs)}")

df = pd.DataFrame(results)
df.to_csv("data/rem_experiment_results.csv", index=False)

print("Saved results.")