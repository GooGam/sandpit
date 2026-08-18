# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Architecture Overview
The project implements a local Retrieval-Augmented Generation (RAG) pipeline:
1. **Text Chunking**: Raw data is processed into smaller, semantically meaningful segments.
2. **Embedding**: Segments are converted into vector representations using a local model (e.g., `embeddinggemma` via Ollama).
3. **Indexing**: Vectors are stored in a local searchable index (e.g., NumPy).
4. **Retrieval**: User queries are embedded and compared against the index to find relevant passages.
5. **Generation**: Retrieved passages are fed into a local LLM (e.g., `gemma 3` via Ollama) to generate a grounded answer.

## Tech Stack
- **Ollama**: Orchestrates local model execution.
- **Embedding Model**: `embeddinggemma`
- **LLM**: `gemma 3`
- **Language**: Python

## Development
As the project currently consists primarily of a conceptual RAG pipeline, standard development workflows (build, test, lint) are being defined. Please ensure any new code follows standard Python practices and adheres to the architecture outlined above.
