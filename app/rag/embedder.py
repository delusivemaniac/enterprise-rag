from sentence_transformers import SentenceTransformer
from app.config import EMBEDDING_MODEL


class Embedder:

    def __init__(self):
        self.model = SentenceTransformer(EMBEDDING_MODEL)

        self.embedding_dimension = len(
            self.model.encode(["test"])[0]
        )

    def generate_embeddings(self, chunks):
        return self.model.encode(chunks)

    def generate_query_embedding(self, query):
        return self.model.encode(query)