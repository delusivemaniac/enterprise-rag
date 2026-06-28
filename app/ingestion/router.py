import os

from .pdf_parser import PDFParser
from .docx_parser import DOCXParser
from .ocr import OCRParser


class DocumentRouter:

    def __init__(self):

        self.pdf_parser = PDFParser()
        self.docx_parser = DOCXParser()
        self.ocr_parser = OCRParser()

    def process(self, file_path):

        extension = os.path.splitext(file_path)[1].lower()

        if extension == ".pdf":
            return self.pdf_parser.parse(file_path)

        elif extension == ".docx":
            return self.docx_parser.parse(file_path)

        else:
            raise ValueError(f"Unsupported file type: {extension}")