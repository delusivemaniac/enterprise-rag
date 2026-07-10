from dataclasses import dataclass,field
from typing import Dict,Any,List

@dataclass
class Page:
    page_number: int
    text: str
    images: List[Any] = field(default_factory=list)
    tables: List[Any] = field(default_factory=list)
    needs_ocr: bool = False

@dataclass
class Document:
    file_name: str
    file_type: str
    pages: List[Page]
    metadata: Dict[str, Any]