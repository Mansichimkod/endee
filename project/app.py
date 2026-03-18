import streamlit as st
from sentence_transformers import SentenceTransformer
import numpy as np

st.set_page_config(page_title="AI Q&A System", page_icon="🤖")

st.title("🤖 AI Document Q&A System")

# Load data
@st.cache_data
def load_data():
    with open("project/data.txt", "r") as f:
        return [line.strip() for line in f if line.strip()]

documents = load_data()

# Load model
@st.cache_resource
def load_model():
    return SentenceTransformer('all-MiniLM-L6-v2')

with st.spinner("⏳ Loading AI model..."):
    model = load_model()

# Compute embeddings
@st.cache_data
def compute_embeddings(docs):
    return model.encode(docs)

with st.spinner("📚 Preparing knowledge base..."):
    doc_embeddings = compute_embeddings(documents)

st.success(f"✅ Ready! Loaded {len(documents)} documents")

# Chat
if "history" not in st.session_state:
    st.session_state.history = []

query = st.text_input("💬 Ask your question:")

if query:
    query_embedding = model.encode([query])
    scores = np.dot(doc_embeddings, query_embedding.T)
    best_index = np.argmax(scores)

    answer = documents[best_index]
    st.session_state.history.append((query, answer))

for q, a in st.session_state.history:
    st.markdown(f"**🧑 You:** {q}")
    st.markdown(f"**🤖 AI:** {a}")
    st.markdown("---")