from app.ingestion.router import DocumentRouter

router = DocumentRouter()

document = router.process(r"C:\Users\Admin\Downloads\JPR question.pdf")

print(document.file_name)
print(len(document.pages))