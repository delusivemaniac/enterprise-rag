import sys

sys.stdout.reconfigure(encoding="utf-8")


print("1. Script started")

from app.ingestion.pdf_parser import PDFParser

print("2. Import successful")

parser = PDFParser()

print("3. Parser created")

document = parser.parse(r"C:\Users\Admin\Documents\frankenstein-mary-shelley.pdf")

print("4. Parse completed")

print(f"File Name: {document.file_name}")
print(f"Pages: {len(document.pages)}")
print(f"Metadata: {document.metadata}")

for page in document.pages:
    print("=" * 50) 
    print(f"Page {page.page_number}")
    print(page.text)   # First 500 characters