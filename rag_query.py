import pickle
import numpy as np
import re
from sklearn.metrics.pairwise import cosine_similarity

# Load stored data
with open("utils/vectorstore.pkl", "rb") as f:
    chunks, vectorizer, vectors = pickle.load(f)

def summarize(text, question):
    """Generate a simple extractive summary of relevant lines."""
    sentences = re.split(r'(?<=[.!?]) +', text)
    question_terms = question.lower().split()
    scored = []
    for s in sentences:
        score = sum(1 for w in question_terms if w in s.lower())
        scored.append((score, s))
    top = sorted(scored, reverse=True)[:2]
    summary = " ".join(s for _, s in top if s.strip())
    return summary or sentences[0][:200]  # fallback

def query_docs(question):
    q_vec = vectorizer.transform([question])
    sims = cosine_similarity(q_vec, vectors).flatten()
    top_indices = sims.argsort()[-2:][::-1]

    print(f"\n🔍 Question: {question}\n")

    best_summary = ""
    for i, idx in enumerate(top_indices, 1):
        path, text = chunks[idx]
        print(f"Result {i} (source: {path}):\n{text.strip()}\n")
        best_summary += summarize(text, question) + " "

    print("💡 Answer Summary:\n" + best_summary.strip())

if __name__ == "__main__":
    while True:
        q = input("\nAsk a question (or 'exit'): ")
        if q.lower() == "exit":
            break
        query_docs(q)
