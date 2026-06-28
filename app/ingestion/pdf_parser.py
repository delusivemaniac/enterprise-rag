import os
import fitz

from .models import Document, Page


class PDFParser:

    def parse(self, file_path: str) -> Document:

        doc = fitz.open(file_path)

        metadata = doc.metadata

        pages = []

        for page_number, page in enumerate(doc):

            text = page.get_text()

            pages.append(
                Page(
                    page_number=page_number + 1,
                    text=text
                )
            )

        return Document(
            file_name=os.path.basename(file_path),
            file_type="pdf",
            pages=pages,
            metadata=metadata
        )