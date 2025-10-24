import os
import pickle
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from sklearn.feature_extraction.text import TfidfVectorizer

def ingest_docs():
    docs = []
    # Load all markdown files from data/docs
    for root, _, files in os.walk("data/docs"):
        for file in files:
            if file.endswith(".md"):
                path = os.path.join(root, file)
                try:
                    content = TextLoader(path).load()[0].page_content
                    docs.append((path, content))
                except Exception as e:
                    print(f"Error loading {path}: {e}")

    # Split documents into smaller chunks
    splitter = RecursiveCharacterTextSplitter(chunk_size=400, chunk_overlap=50)
    chunks = []
    for path, content in docs:
        for chunk in splitter.split_text(content):
            chunks.append((path, chunk))

    # Create a TF-IDF vector representation for each chunk
    texts = [chunk for _, chunk in chunks]
    vectorizer = TfidfVectorizer(stop_words="english").fit(texts)
    vectors = vectorizer.transform(texts)

    # Save chunks, vectorizer, and vectors
    os.makedirs("utils", exist_ok=True)
    with open("utils/vectorstore.pkl", "wb") as f:
        pickle.dump((chunks, vectorizer, vectors), f)

    print(f"✅ Indexed {len(chunks)} text chunks into utils/vectorstore.pkl")

if __name__ == "__main__":
    ingest_docs()
