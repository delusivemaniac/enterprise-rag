from app.ingestion.router import DocumentRouter
from app.rag.chunker import Chunker

print("Test started")

router = DocumentRouter()
document = router.process(r"documents\JPR question.pdf")

chunker = Chunker()
chunks = chunker.chunk_document(document)

print(f"\nTotal Chunks: {len(chunks)}\n")

for chunk in chunks:
    print("=" * 100)
    print(f"Chunk ID      : {chunk.chunk_id}")
    print(f"Document      : {chunk.document_name}")
    print(f"Page Number   : {chunk.page_number}")
    print("-" * 100)
    print(chunk.text)
    print()