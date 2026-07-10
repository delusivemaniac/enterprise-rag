from dataclasses import dataclass

from dataclasses import dataclass

from app.ingestion.models import Document

from llama_index.core import Document as LlamaIndexDocument
from llama_index.core.node_parser import SemanticSplitterNodeParser
from llama_index.embeddings.huggingface import HuggingFaceEmbedding


@dataclass
class Chunk:
    chunk_id: int
    text: str
    document_name: str
    page_number: int


class Chunker:

    def __init__(self):

        print("Loading BGE-M3 embedding model...")

        self.embed_model = HuggingFaceEmbedding(
            model_name="BAAI/bge-m3"
        )

        print("Creating Semantic Splitter...")

        self.splitter = SemanticSplitterNodeParser(
            embed_model=self.embed_model,
            breakpoint_percentile_threshold=95
        )

    def chunk_document(self, document: Document):

        print("Generating semantic chunks...")

        chunks = []
        chunk_id = 0

        for page in document.pages:

            llama_document = LlamaIndexDocument(
                text=page.text,
                metadata={
                    "page": page.page_number,
                    "document": document.file_name
                }
            )

            nodes = self.splitter.get_nodes_from_documents(
                [llama_document]
            )

            for node in nodes:

                chunks.append(
                    Chunk(
                        chunk_id=chunk_id,
                        text=node.text.strip(),
                        document_name=document.file_name,
                        page_number=page.page_number
                    )
                )

                chunk_id += 1

        return chunks