# 🤖 AI Document Q&A System (Endee Project)

## 📌 Project Overview

This project is an AI-powered Question Answering system that retrieves relevant answers from a predefined dataset using semantic search.

It uses sentence embeddings to understand the meaning of user queries and returns the most relevant answer from the dataset.

---

## 🚀 Features

* 🔍 Semantic search using embeddings
* 🤖 AI-based question answering
* 💬 Chat-like interface using Streamlit
* ⚡ Fast retrieval using precomputed embeddings
* 📂 Uses a custom dataset (`data.txt`)

---

## 🧠 How It Works

1. The dataset is loaded from `data.txt`
2. Each sentence is converted into vector embeddings using a transformer model
3. User query is also converted into an embedding
4. Cosine similarity (via dot product) is used to find the closest match
5. The most relevant answer is returned

---

## 🧰 Technologies Used

* Python
* Streamlit (Frontend UI)
* Sentence Transformers
* NumPy

---

## 📦 Use of Endee Vector Database

This project is built as part of the Endee evaluation.
While the current implementation uses in-memory embeddings for semantic search, the same workflow can be integrated with Endee Vector Database for scalable and efficient vector storage and retrieval.

---

## 📁 Project Structure

```
endee/
│── project/
│   │── app.py          # Streamlit frontend
│   │── data.txt        # Dataset
│── README.md
```

---

## ▶️ How to Run the Project

### Step 1: Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/endee.git
cd endee
```

### Step 2: Install Dependencies

```bash
pip install streamlit sentence-transformers numpy
```

### Step 3: Run Application

```bash
streamlit run project/app.py
```

### Step 4: Open in Browser

```
http://localhost:8501
```

---

## 💡 Example Use Cases

* AI-based FAQ system
* Knowledge retrieval system
* Educational assistant
* Basic chatbot

---

## 📊 Future Improvements

* 🔗 Integrate Endee vector database fully
* 📄 Add PDF/document support
* 🧠 Improve answer generation using LLMs
* 🌐 Deploy online

---

## 👩‍💻 Author

Mansi Chimkod

---

