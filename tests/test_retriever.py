from app.api.retriever import Retriever
from app.config import DEFAULT_TOP_K

retriever = Retriever()

query_embedding = retriever.embedder.generate_query_embedding(
    "What is this document about?"
)

results = retriever.client.query_points(
    collection_name="enterprise_rag",
    query=query_embedding.tolist(),
    limit=DEFAULT_TOP_K,
).points

for point in results:
    print(point.payload)