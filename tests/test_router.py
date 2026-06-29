import sys
sys.stdout.reconfigure(encoding="utf-8")

from app.ingestion.router import DocumentRouter

router = DocumentRouter()

document = router.process(r"C:\enterprise-rag\documents\JPR question.pdf")

print(document.file_name)
print(document.file_type)
print(len(document.pages))