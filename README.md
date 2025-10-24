# Mini DocsGPT — Build Your Own Local RAG System (No API Keys Needed)

This project shows you how to build a Retrieval-Augmented Generation (RAG) system completely offline and easy to understand. It’s like a mini version of ChatGPT that answers questions using your own documentation.

No OpenAI keys.  
No internet connection required.  
No machine learning background needed.

## What This Project Does

Mini DocsGPT can:
- Read your Markdown documentation files (.md)
- Break them into smaller chunks
- Index them so they can be searched efficiently
- Let you ask natural-language questions like “How does authentication work?”
- Return the most relevant passages with a short summary, all from your local files.

You’ll also get a clean web interface powered by Gradio.

## What You’ll Learn

By completing this project, you’ll learn the core parts of how RAG systems work:
1. Document ingestion — reading and splitting text
2. Vectorization — turning text into searchable numerical form
3. Retrieval — finding the most relevant content
4. Summarization — generating a short, readable answer

## Getting Started

These instructions will guide you through setting it up on your own computer.

### 1. Install Python

You’ll need Python 3.10 or newer. To check if it’s installed, open a terminal and type:
```bash
python3 --version
If it’s missing, download it from https://www.python.org/downloads/
.

2. Set Up Your Project Folder

Open your terminal and create a folder for the project:
mkdir docs-gpt
cd docs-gpt

3. Create a Virtual Environment

A “virtual environment” keeps your project’s Python packages isolated from your system.
python3 -m venv venv
source venv/bin/activate
You should now see (venv) at the start of your terminal prompt.

4. Install Dependencies

These are the small Python libraries this project uses.
pip install langchain langchain-community langchain-text-splitters scikit-learn gradio
5. Add Example Docs

Create some simple Markdown files inside data/docs/:
mkdir -p data/docs
then add your markdown files.
6. Index Your Documents

This step builds a local search index using utils/ingest_docs.py.
python3 utils/ingest_docs.py
you should see
Indexed 6 text chunks into utils/vectorstore.pkl

7. Launch the Web App

Now run:
python3 app.py

Gradio will start a local web server and show a link such as:
Running on local URL: http://127.0.0.1:7860

8. Ask a Question

Try typing:

How does authentication work?


You’ll get a short summary and the source text from your docs.

How It Works (Simplified)

Here’s what’s happening behind the scenes:

Ingestion (utils/ingest_docs.py)

Reads all .md files under data/docs/

Splits them into small chunks

Turns them into searchable vectors using TF-IDF

Saves everything into utils/vectorstore.pkl

Querying (app.py or rag_query.py)

When you ask a question, your query is vectorized the same way

The system finds the most similar text chunks

A simple summarizer extracts the key lines to form a natural answer

Customize It

You can:

Replace data/docs/ with your own documentation

Change the chunk size in ingest_docs.py for finer or coarser search

Modify the summarizer in rag_query.py to improve phrasing

Deploy this to Hugging Face Spaces (it works perfectly there)
Credits

Built with:

LangChain

Scikit-learn

Gradio

Created as a learning project for understanding the fundamentals of RAG systems without needing cloud APIs or complex machine learning setups.

Mini DocsGPT — your first step into Retrieval-Augmented Generation.