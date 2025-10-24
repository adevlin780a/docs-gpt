import pickle
import re
import numpy as np
import gradio as gr
from sklearn.metrics.pairwise import cosine_similarity

# Load pre-built vectorstore
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
    return summary or sentences[0][:200]

def query_docs(question):
    """Retrieve and summarize relevant chunks."""
    q_vec = vectorizer.transform([question])
    sims = cosine_similarity(q_vec, vectors).flatten()
    top_indices = sims.argsort()[-2:][::-1]

    results_text = ""
    best_summary = ""

    for idx in top_indices:
        path, text = chunks[idx]
        results_text += f"### Source: `{path}`\n{text.strip()}\n\n"
        best_summary += summarize(text, question) + " "

    answer = best_summary.strip()
    if not answer:
        answer = "I couldn’t find anything relevant in your docs."
    return answer, results_text

# Define Gradio interface
demo = gr.Interface(
    fn=query_docs,
    inputs=gr.Textbox(label="Ask a question about your docs"),
    outputs=[
        gr.Textbox(label="💡 Summary Answer", lines=3),
        gr.Markdown(label="📚 Retrieved Context")
    ],
    title="Mini DocsGPT (Offline RAG Demo)",
    description="Ask natural questions about your local Markdown documentation.",
    theme="soft",
    allow_flagging="never",
)

if __name__ == "__main__":
    demo.launch()
