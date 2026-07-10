from qdrant_client import QdrantClient

from app.config import (
    COLLECTION_NAME,
    QDRANT_PATH,
)

from app.rag.embedder import Embedder


class Retriever:

    def __init__(self):

        self.client = QdrantClient(path=QDRANT_PATH)

        self.embedder = Embedder()

    def search(self, question: str, top_k: int):

        query_embedding = self.embedder.generate_query_embedding(question)

        results = self.client.query_points(
            collection_name=COLLECTION_NAME,
            query=query_embedding.tolist(),
            limit=top_k,
        ).points

        return [
            {
                "text": point.payload["text"],
                "score": point.score,
                "chunk_id": point.payload.get("chunk_id"),
                "document_name": point.payload.get("document_name"),
                "page_number": point.payload.get("page_number"),
            }
            for point in results
        ]