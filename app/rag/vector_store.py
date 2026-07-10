from qdrant_client import QdrantClient
from qdrant_client.models import (
    Distance,
    VectorParams,
    PointStruct,
)

from app.config import (
    COLLECTION_NAME,
    QDRANT_PATH,
)


class VectorStore:

    def __init__(self, embedding_dimension: int):

        self.client = QdrantClient(path=QDRANT_PATH)

        self.collection_name = COLLECTION_NAME

        self.embedding_dimension = embedding_dimension

        self._create_collection()

    def _create_collection(self):

        self.client.recreate_collection(
            collection_name=self.collection_name,
            vectors_config=VectorParams(
                size=self.embedding_dimension,
                distance=Distance.COSINE,
            ),
        )

    def store(self, chunks, embeddings):

        points = []

        for chunk, embedding in zip(chunks, embeddings):

            points.append(
                PointStruct(
                    id=chunk.chunk_id,
                    vector=embedding.tolist(),
                    payload={
                        "text": chunk.text,
                        "chunk_id": chunk.chunk_id,
                        "document_name": chunk.document_name,
                        "page_number": chunk.page_number,
                    }
                )
            )

        self.client.upsert(
            collection_name=self.collection_name,
            points=points,
        )

        print(f"Stored {len(points)} vectors successfully.")