import os
import fitz
import pdfplumber

from .models import Document, Page


class PDFParser:

    def parse(self, file_path: str) -> Document:

        with fitz.open(file_path) as doc, pdfplumber.open(file_path) as plumber_pdf:

            metadata = doc.metadata
            pages = []

            for page_number, page in enumerate(doc):

                needs_ocr = self._needs_ocr(page)

                if needs_ocr:
                    text = "[OCR Placeholder]"
                else:
                    # Better reading order
                    text = page.get_text(sort=True)

                    # Extract tables
                    table_text = self._extract_tables(
                        plumber_pdf,
                        page_number
                    )

                    if table_text:
                        text += "\n\n" + table_text

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
        text = page.get_text(sort=True).strip()
        return len(text) < 20

    def _extract_tables(self, plumber_pdf, page_number: int) -> str:
        """
        Extract tables from a page and convert them into readable text.
        """

        page = plumber_pdf.pages[page_number]

        tables = page.extract_tables()

        if not tables:
            return ""

        table_text = []

        for table in tables:

            table_text.append("[TABLE]")

            for row in table:
                row = [
                    cell.strip() if cell else ""
                    for cell in row
                ]

                table_text.append(" | ".join(row))

            table_text.append("")

        return "\n".join(table_text)