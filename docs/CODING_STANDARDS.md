# PolyDoc AI - Coding Standards

Version: 1.0

---

# Purpose

This document defines the coding standards for the PolyDoc AI project.

Every developer and AI coding assistant must follow these standards.

The objective is to maintain a clean, scalable, readable, and production-ready codebase.

These standards apply to every Python module in this repository.

---

# Python Version

Python 3.12+

---

# General Principles

Always write production-quality code.

Code should prioritize

- Readability
- Maintainability
- Modularity
- Scalability

Avoid writing code that only works for the current feature.

Always consider future extensibility.

---

# Naming Conventions

## Variables

Use snake_case.

Example

```python
document_loader
chunk_size
vector_store
```

Avoid

```python
DocLoader
ChunkSize
x
temp1
```

---

## Functions

Use snake_case.

Functions should describe actions.

Examples

```python
load_pdf()

create_embeddings()

detect_language()

translate_text()

retrieve_documents()
```

---

## Classes

Use PascalCase.

Examples

```python
PDFLoader

EmbeddingService

VectorStore

Retriever
```

---

## Constants

Use UPPER_CASE.

Examples

```python
DEFAULT_CHUNK_SIZE

SUPPORTED_LANGUAGES

UPLOAD_DIRECTORY
```

---

## Files

Use snake_case.

Examples

```text
pdf_loader.py

prompt_builder.py

vector_store.py
```

Avoid

```text
PdfLoader.py

VectorStore.py

NewFile.py
```

---

# Code Organization

Every file must have one responsibility.

Every class should represent one concept.

Every function should perform one task.

Prefer multiple small functions over one large function.

---

# Function Rules

Functions should

- Perform one responsibility
- Have descriptive names
- Include type hints
- Include docstrings
- Raise meaningful exceptions

Maximum recommended length

40 lines

If a function grows larger,

consider splitting it.

---

# Class Rules

Classes should

- Encapsulate one responsibility
- Avoid unnecessary inheritance
- Use dependency injection when appropriate

Maximum recommended size

300 lines

---

# Type Hints

Always use type hints.

Example

```python
def load_pdf(file_path: Path) -> list[Document]:
```

Never omit type hints in public functions.

---

# Docstrings

Every public function must include

Description

Args

Returns

Raises

Example

```python
def load_pdf(file_path: Path) -> list[Document]:
    """
    Load a PDF document.

    Args:
        file_path:
            Path to the PDF file.

    Returns:
        List of LangChain Document objects.

    Raises:
        FileNotFoundError:
            If the PDF does not exist.
    """
```

---

# Comments

Only explain WHY.

Never explain WHAT.

Good

```python
# Preserve metadata for future citations.
```

Bad

```python
# Increment i
i += 1
```

---

# Logging

Use logging.

Avoid print() except in temporary local debugging.

Good

```python
logger.info("PDF loaded successfully.")
```

Bad

```python
print("Done")
```

---

# Error Handling

Always raise meaningful exceptions.

Good

```python
raise FileNotFoundError(...)
```

Never

```python
except:
    pass
```

Never suppress exceptions silently.

---

# Imports

Standard Library

↓

Third-party packages

↓

Local imports

Example

```python
from pathlib import Path

import logging

from langchain_core.documents import Document

from rag.chunking import TextChunker
```

---

# Dependency Rules

Modules may only communicate through their public interfaces.

Never access internal implementation details of another module.

---

# Architecture Rules

Do not mix responsibilities.

Example

PDF Loader

May

✔ Load PDFs

Must NOT

✘ Generate embeddings

✘ Query Ollama

✘ Chunk text

---

Chunker

May

✔ Split documents

Must NOT

✘ Generate embeddings

---

Retriever

May

✔ Query FAISS

Must NOT

✘ Build prompts

✘ Generate responses

---

LLM Module

May

✔ Send prompts to Ollama

Must NOT

✘ Retrieve vectors

---

# Configuration

Never hardcode

- Paths
- Model names
- API URLs
- Chunk sizes

Store configuration in

config/settings.py

---

# Testing

Code should be independently testable.

Avoid tightly coupled modules.

Do not mix file I/O with business logic.

---

# Git Commit Style

Use Conventional Commits.

Examples

feat:

fix:

docs:

refactor:

test:

chore:

Example

feat: implement PDF loader

docs: add system architecture

fix: preserve page metadata

---

# Code Quality Checklist

Before considering a file complete

✓ PEP8 compliant

✓ Type hints

✓ Docstrings

✓ Logging

✓ Exception handling

✓ No duplicated code

✓ Single Responsibility Principle

✓ Easy to test

✓ Matches project architecture

✓ Ready for production

---

# Engineering Philosophy

Readable code is better than clever code.

Small modules are better than large modules.

Composition is preferred over inheritance.

Architecture is more important than shortcuts.

Every commit should improve the project.

Write code that another engineer can understand six months later.