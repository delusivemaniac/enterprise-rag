# Enterprise Document RAG Pipeline

An enterprise-ready Retrieval-Augmented Generation (RAG) pipeline for intelligent document processing and semantic information retrieval.

This project combines document ingestion, semantic chunking, embedding generation, vector storage, and semantic retrieval to enable efficient context-aware search over enterprise documents.

---

## Features

- PDF Parsing using PyMuPDF
- DOCX Parsing
- OCR Detection (Placeholder for future integration)
- Table Extraction from PDFs
- Semantic Chunking using LlamaIndex
- BGE-M3 Embedding Model
- Qdrant Vector Database Integration
- Semantic Retrieval
- Page-level Metadata Preservation
- Document-level Metadata Preservation
- Modular Pipeline Architecture
- Unit Tests for Individual Components

---

# Architecture

```text
                     Enterprise Document

                  PDF / DOCX Document
                           │
                           ▼
                 ┌─────────────────────┐
                 │ Document Parser     │
                 └─────────────────────┘
                           │
        ┌──────────────────┼──────────────────┐
        │                  │                  │
        ▼                  ▼                  ▼
 Text Extraction     Table Extraction    OCR Detection
                                               │
                                               ▼
                                   (Future Implementation)

                           │
                           ▼
              ┌──────────────────────────┐
              │ Semantic Chunking        │
              │ BGE-M3 + LlamaIndex      │
              └──────────────────────────┘
                           │
                           ▼
              ┌──────────────────────────┐
              │ Embedding Generation     │
              │ BGE-M3 SentenceTransformer│
              └──────────────────────────┘
                           │
                           ▼
              ┌──────────────────────────┐
              │ Qdrant Vector Database   │
              └──────────────────────────┘
                           │
                           ▼
              ┌──────────────────────────┐
              │ Semantic Retriever       │
              └──────────────────────────┘
                           │
                           ▼
                 Most Relevant Chunks
```

---

# Project Structure

```text
enterprise-rag/
│
├── app/
│   ├── api/
│   ├── ingestion/
│   │   ├── pdf_parser.py
│   │   ├── docx_parser.py
│   │   ├── ocr.py
│   │   ├── router.py
│   │   └── models.py
│   │
│   ├── rag/
│   │   ├── chunker.py
│   │   ├── embedder.py
│   │   ├── retriever.py
│   │   └── vector_store.py
│   │
│   └── config.py
│
├── documents/
│
├── tests/
│
└── README.md
```

---

# Technologies Used

| Technology | Purpose |
|------------|---------|
| Python | Backend Development |
| PyMuPDF | PDF Text Extraction |
| pdfplumber | Table Extraction |
| python-docx | DOCX Parsing |
| LlamaIndex | Semantic Chunking |
| BGE-M3 | Embedding Model |
| Sentence Transformers | Embedding Generation |
| Qdrant | Vector Database |
| Hugging Face | Model Hosting |

---

# Pipeline Workflow

```text
Document Upload
        │
        ▼
Document Parsing
        │
        ▼
Text Extraction
        │
        ▼
Semantic Chunking
        │
        ▼
Embedding Generation
        │
        ▼
Vector Storage (Qdrant)
        │
        ▼
User Query
        │
        ▼
Query Embedding
        │
        ▼
Semantic Retrieval
        │
        ▼
Most Relevant Chunks
```

---

# Semantic Chunking

Instead of traditional fixed-size chunking, this project implements **semantic chunking** using **LlamaIndex's SemanticSplitterNodeParser** with the **BAAI BGE-M3** embedding model.

Benefits include:

- Context-aware chunk boundaries
- Better semantic coherence
- Improved retrieval quality
- Reduced context fragmentation
- Page-wise chunk generation
- Metadata preservation

Each chunk stores:

- Chunk ID
- Document Name
- Page Number
- Chunk Text

---

# Installation

Clone the repository:

```bash
git clone https://github.com/delusivemaniac/enterprise-rag.git

cd enterprise-rag
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

# Running Tests

### Test PDF Parsing

```bash
python -m tests.test_pdf
```

### Test Semantic Chunking

```bash
python -m tests.test_chunker
```

### Test Vector Storage

```bash
python -m tests.test_vector_store
```

### Test Retrieval

```bash
python -m tests.test_retriever
```

---

# Current Capabilities

- Parse PDF documents
- Parse DOCX documents
- Detect scanned pages
- Extract tables
- Generate semantic chunks
- Generate vector embeddings
- Store embeddings in Qdrant
- Retrieve relevant document chunks
- Preserve document metadata

---

# Future Improvements

- OCR Integration (Tesseract / PaddleOCR)
- FastAPI REST API
- Hybrid Search (Dense + Sparse Retrieval)
- Metadata Filtering
- Re-ranking Models
- Support for PPTX, XLSX and Images
- Multi-document Query Support
- Streaming LLM Responses

---

# Example Retrieval Output

```text
Question:
What are the features of Java?

Retrieved Chunk:
List any four features of Java.

Source:
Document : JPR question.pdf
Page     : 1
```

---

# Why Semantic Chunking?

Traditional chunking methods split documents using character count or token limits, often breaking logical context.

Semantic chunking identifies natural semantic boundaries using embedding similarity, resulting in more coherent chunks and improved retrieval accuracy.

---

# License

This project is intended for educational and research purposes.

---

# Author

**Tejasvi**

Enterprise Document RAG Pipeline using Semantic Chunking and Qdrant Vector Database.
