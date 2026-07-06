from sentence_transformers import SentenceTransformer
from qdrant_client import QdrantClient

# Load embedding model
model = SentenceTransformer(
    "BAAI/bge-small-en-v1.5"
)

# Connect to local Qdrant database
client = QdrantClient(path="./qdrant_db")

# User query
query = input("Ask a question: ")

# Convert query to embedding
query_vector = model.encode(query)

# Search
results = client.query_points(
    collection_name="frankenstein",
    query=query_vector.tolist(),
    limit=3
).points

# Display retrieved chunks
for i, result in enumerate(results):
    print(f"\nRESULT {i+1}")
    print("=" * 50)
    print(result.payload["text"])