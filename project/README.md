# 🚀 AI RAG Project using Endee Vector Database

## 📌 Project Overview

This project is a simple **Retrieval-Augmented Generation (RAG)** system built using the Endee vector database. It allows users to ask questions and retrieves the most relevant answer from stored data using semantic search.

The goal of this project is to demonstrate how vector databases like Endee can be used in real-world AI applications such as question answering systems.

---

## ⚙️ Features

* Semantic search using embeddings
* Simple question-answering system
* Lightweight and beginner-friendly implementation
* Demonstrates practical usage of vector database concepts

---

## 🧠 How It Works

1. Text data is stored and converted into vector embeddings
2. User enters a query
3. The query is converted into an embedding
4. Similarity is calculated between query and stored data
5. The most relevant result is returned as the answer

---

## 🗂️ Project Structure

```
project/
│── main.py
│── data.txt
│── requirements.txt
│── README.md
```

---

## 🛠️ Technologies Used

* Python
* Sentence Transformers
* NumPy
* Endee Vector Database

---

## 🔗 Use of Endee

In this project, Endee is used as a vector database to:

* Store embeddings of text data
* Perform similarity search
* Retrieve relevant information efficiently

---

## ▶️ How to Run the Project

### Step 1: Clone the repository

```
git clone https://github.com/YOUR_USERNAME/endee.git
cd endee
```

### Step 2: Install dependencies

```
pip install -r requirements.txt
```

### Step 3: Run the project

```
python main.py
```

### Step 4: Ask a question

Example:

```
What is AI?
```

---

## 📊 Example Output

```
Ask something: What is AI?
Answer: Artificial Intelligence is the simulation of human intelligence.
```

---

## 🎯 Conclusion

This project demonstrates a basic implementation of a RAG system using Endee. It can be extended to build advanced AI applications such as chatbots, recommendation systems, and document search engines.

---

## 👩‍💻 Author

Your Name
