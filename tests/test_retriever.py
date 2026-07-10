from app.api.retriever import Retriever
from app.config import DEFAULT_TOP_K

retriever = Retriever()

results = retriever.search(
    question="What is this document about?",
    top_k=DEFAULT_TOP_K,
)

print(f"Retrieved {len(results)} chunks\n")

for i, result in enumerate(results):
    print("=" * 60)
    print(f"Result {i+1}")
    print(f"Score: {result['score']:.4f}")
    print(f"Chunk ID: {result['chunk_id']}")
    print(result["text"][:500])