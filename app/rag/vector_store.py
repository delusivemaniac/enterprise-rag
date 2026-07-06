import fitz
from sentence_transformers import SentenceTransformer
from qdrant_client import QdrantClient
from qdrant_client.models import Distance, VectorParams, PointStruct

# Extract text
pdf = fitz.open("data/frankenstein-mary-shelley.pdf")

text = ""
for page in pdf:
    text += page.get_text()

# Chunk text
chunk_size = 1000
chunk_overlap = 200

chunks = []

start = 0
while start < len(text):
    end = start + chunk_size
    chunks.append(text[start:end])
    start += chunk_size - chunk_overlap

print(f"Chunks: {len(chunks)}")

# Embeddings
model = SentenceTransformer("BAAI/bge-small-en-v1.5")
embeddings = model.encode(chunks)

# Create Qdrant database
client = QdrantClient(path="./qdrant_db")

client.recreate_collection(
    collection_name="frankenstein",
    vectors_config=VectorParams(
        size=384,
        distance=Distance.COSINE
    )
)

# Store vectors
points = []

for i, embedding in enumerate(embeddings):
    points.append(
        PointStruct(
            id=i,
            vector=embedding.tolist(),
            payload={"text": chunks[i]}
        )
    )

client.upsert(
    collection_name="frankenstein",
    points=points
)

print("Vectors stored successfully!")