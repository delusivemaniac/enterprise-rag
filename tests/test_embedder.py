from app.ingestion.router import DocumentRouter
from app.rag.chunker import Chunker
from app.rag.embedder import Embedder

router = DocumentRouter()
document = router.process(r"documents\JPR question.pdf")

chunker = Chunker()
chunks = chunker.chunk_document(document)

embedder = Embedder()

embeddings = embedder.generate_embeddings(chunks)

print(f"Chunks: {len(chunks)}")
print(f"Embeddings: {len(embeddings)}")
print(f"Embedding Dimension: {embedder.embedding_dimension}")