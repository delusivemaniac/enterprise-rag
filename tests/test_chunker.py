from app.ingestion.router import DocumentRouter
from app.rag.chunker import Chunker

print("Test started")

router = DocumentRouter()
document = router.process(r"C:\enterprise-rag\documents\JPR question.pdf")

chunker = Chunker()

chunks = chunker.chunk_document(document)

print(f"Total Chunks: {len(chunks)}")

for i, chunk in enumerate(chunks[:3]):
    print("=" * 50)
    print(f"Chunk {i+1}")
    print(chunk[:300])