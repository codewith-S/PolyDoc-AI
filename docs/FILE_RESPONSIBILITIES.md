# File Responsibilities

## Purpose

This document defines the responsibility of every file in the PolyDoc AI project.

Every file must have **one clear responsibility**.

A file should only perform the tasks assigned to it.

This document serves as the source of truth for both developers and AI coding assistants.

When generating code, always follow these responsibilities.

---

# RAG MODULE

---

## rag/loaders/pdf_loader.py

### Purpose

Load PDF files and convert them into LangChain `Document` objects.

### Responsibilities

- Validate PDF file existence
- Load PDFs using PyPDFLoader
- Preserve document metadata
- Return `List[Document]`

### Must NOT

- Chunk text
- Clean text
- Generate embeddings
- Store vectors
- Translate content
- Call the LLM
- Retrieve documents

### Output

```python
List[Document]
```

---

## rag/chunking/text_chunker.py

### Purpose

Split LangChain Documents into semantic chunks.

### Responsibilities

- Accept `List[Document]`
- Split using `RecursiveCharacterTextSplitter`
- Preserve metadata
- Configurable chunk size
- Configurable overlap

### Must NOT

- Load PDFs
- Generate embeddings
- Store vectors
- Retrieve documents
- Translate text

### Output

```python
List[Document]
```

---

## rag/embeddings/embedder.py

### Purpose

Convert document chunks into vector embeddings.

### Responsibilities

- Load embedding model
- Generate embeddings
- Return embeddings
- Support configurable embedding model

### Must NOT

- Load PDFs
- Chunk text
- Store vectors
- Retrieve vectors
- Call Ollama

### Output

```python
List[Vector]
```

---

## rag/retrieval/vector_store.py

### Purpose

Manage the FAISS vector database.

### Responsibilities

- Create FAISS index
- Store embeddings
- Save index
- Load index
- Delete index

### Must NOT

- Generate embeddings
- Retrieve answers
- Build prompts

---

## rag/retrieval/retriever.py

### Purpose

Retrieve the most relevant document chunks using semantic similarity.

### Responsibilities

- Query FAISS
- Perform similarity search
- Return Top-K relevant chunks
- Preserve metadata

### Must NOT

- Generate answers
- Call Ollama
- Translate text

### Output

```python
List[Document]
```

---

## rag/prompts/prompt_builder.py

### Purpose

Construct prompts for the language model.

### Responsibilities

- Combine retrieved context
- Add user query
- Build system prompt
- Prepare final prompt

### Must NOT

- Retrieve vectors
- Translate
- Call FastAPI
- Load PDFs

### Output

```python
str
```

---

## rag/llm/ollama_client.py

### Purpose

Provide an interface to the local Ollama server.

### Responsibilities

- Connect to Ollama
- Send prompt
- Receive response
- Handle model errors

### Must NOT

- Retrieve vectors
- Build prompts
- Translate
- Process PDFs

### Output

```python
str
```

---

## rag/translation/language_detector.py

### Purpose

Detect the language of user queries.

### Responsibilities

- Detect language
- Return ISO language code

### Must NOT

- Translate
- Retrieve
- Generate answers

### Output

```python
str
```

---

## rag/translation/translator.py

### Purpose

Translate user input and model responses.

### Responsibilities

- Translate to English
- Translate from English
- Preserve meaning
- Support English, Hindi and Marathi

### Must NOT

- Detect language
- Call Ollama
- Retrieve vectors

### Output

```python
str
```

---

## rag/evaluation/evaluator.py

### Purpose

Evaluate retrieval and answer quality.

### Responsibilities

- Evaluate retrieval accuracy
- Evaluate grounding
- Evaluate citation quality

### Must NOT

- Retrieve
- Generate answers
- Store vectors

---

# BACKEND MODULE

---

## backend/app/routes/upload.py

### Purpose

Handle document uploads.

### Responsibilities

- Receive uploaded files
- Validate file type
- Save files
- Trigger ingestion pipeline

### Must NOT

- Process PDFs directly
- Generate embeddings

---

## backend/app/routes/chat.py

### Purpose

Handle chat requests.

### Responsibilities

- Receive user query
- Call retrieval pipeline
- Return AI response

### Must NOT

- Implement retrieval logic
- Build prompts
- Translate

---

## backend/app/services/document_service.py

### Purpose

Coordinate the complete document ingestion workflow.

### Responsibilities

- Call loader
- Call chunker
- Call embedder
- Store vectors

### Must NOT

- Expose API endpoints
- Handle UI

---

## backend/app/services/chat_service.py

### Purpose

Coordinate the complete chat workflow.

### Responsibilities

- Detect language
- Translate if required
- Retrieve documents
- Build prompt
- Query Ollama
- Translate response
- Return citations

### Must NOT

- Handle HTTP requests
- Manage uploads

---

# FRONTEND MODULE

---

## frontend/app.py

### Purpose

Main Streamlit application.

### Responsibilities

- Upload documents
- Display chat
- Display citations
- Display history

### Must NOT

- Implement AI logic
- Generate embeddings
- Query FAISS directly

---

# STORAGE MODULE

---

## storage/vector_db/

Stores FAISS indexes.

No application logic.

---

## storage/metadata/

Stores SQLite metadata.

No business logic.

---

# GENERAL RULES

Every file should

✔ Have one responsibility

✔ Be independently testable

✔ Include logging

✔ Include type hints

✔ Include docstrings

✔ Raise meaningful exceptions

Never

✘ Duplicate business logic

✘ Access unrelated modules

✘ Mix UI and AI logic

✘ Mix retrieval and generation

✘ Break the project architecture