from app.ingestion.router import DocumentRouter
from app.rag.chunker import Chunker
from app.rag.embedder import Embedder
from app.rag.vector_store import VectorStore

router = DocumentRouter()
document = router.process(r"documents\JPR question.pdf")

chunker = Chunker()
chunks = chunker.chunk_document(document)

embedder = Embedder()
embeddings = embedder.generate_embeddings(chunks)

vector_store = VectorStore(
    embedding_dimension=embedder.embedding_dimension
)

vector_store.store(chunks, embeddings)

print("Pipeline completed successfully.")