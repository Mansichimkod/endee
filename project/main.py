id="proj1"
from sentence_transformers import SentenceTransformer
import numpy as np

# simple data
documents = [
    "Artificial Intelligence is the simulation of human intelligence.",
    "Machine Learning is a subset of AI.",
    "Deep Learning uses neural networks."
]

# load model
model = SentenceTransformer('all-MiniLM-L6-v2')

# convert to embeddings
doc_embeddings = model.encode(documents)

# user query
query = input("Ask something: ")
query_embedding = model.encode([query])

# similarity
scores = np.dot(doc_embeddings, query_embedding.T)

# best match
best_index = np.argmax(scores)

print("Answer:", documents[best_index])