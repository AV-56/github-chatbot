# RAG Chatbot Task List

**Tech Stack:**
- Python 3.10
- Framework: LangChain
- Vector Database: FAISS
- LLM: Google Gemini
- UI: Streamlit

## Phase 1: Setup
- [x] Create conda environment `github-chatbot`
- [x] Create `requirements.txt`, `.env`, and `main.py`
- [x] Install dependencies
- [ ] Get a Google Gemini API Key

## Phase 2: Data Ingestion
- [ ] Write code to fetch/clone a GitHub repository
- [ ] Load files into LangChain Document objects

## Phase 3: Chunking
- [ ] Split documents into smaller chunks using LangChain text splitters

## Phase 4: Embeddings & Vector DB
- [ ] Generate embeddings using Gemini Embeddings
- [ ] Store chunks and embeddings in FAISS

## Phase 5: Retrieval & Generation
- [ ] Set up the LangChain QA chain
- [ ] Test the pipeline with a question

## Phase 6: User Interface
- [ ] Build a Streamlit chat interface
