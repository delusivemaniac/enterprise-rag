import os
import fitz

from .models import Document, Page


class PDFParser:

    def parse(self, file_path: str) -> Document:

        doc = fitz.open(file_path)

        metadata = doc.metadata

        pages = []
        
        

        for page_number, page in enumerate(doc):

            needs_ocr = self._needs_ocr(page)

            if needs_ocr:
                text = "[OCR Placeholder]"
            else:
                text = page.get_text()

            pages.append(
                Page(
                      page_number=page_number + 1,
                      text=text,
                      needs_ocr=needs_ocr
                )
             )

        return Document(
            file_name=os.path.basename(file_path),
            file_type="pdf",
            pages=pages,
            metadata=metadata
        )

    def _needs_ocr(self, page) -> bool:
        """
        Returns True if the page has little or no extractable text.
        """
        text = page.get_text().strip()
        return len(text) < 20