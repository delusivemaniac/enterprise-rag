import fitz
from sentence_transformers import SentenceTransformer

# Load PDF
pdf = fitz.open("data/frankenstein-mary-shelley.pdf")

text = ""

for page in pdf:
    text += page.get_text()

# Chunking
chunk_size = 1000
chunk_overlap = 200

chunks = []

start = 0

while start < len(text):
    end = start + chunk_size
    chunks.append(text[start:end])
    start += chunk_size - chunk_overlap

print(f"Total chunks: {len(chunks)}")

# Load embedding model
model = SentenceTransformer(
    "BAAI/bge-small-en-v1.5"
)

print("Embedding model loaded.")

# Generate embeddings
embeddings = model.encode(chunks)

print("Embeddings generated.")

print("Embedding shape:")
print(len(embeddings))
print(len(embeddings[0]))