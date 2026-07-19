# 🤖 Dynamic GitHub Repo Chatbot

This is a full-stack Retrieval-Augmented Generation (RAG) application that allows you to chat with any public GitHub repository using natural language. It dynamically clones the repository, processes the code, and uses Google Gemini to answer questions based strictly on the codebase.

## 🚀 Features
- **Dynamic Ingestion**: Paste any public GitHub URL and Branch Name. The app will automatically clone it into an isolated temporary directory.
- **Multi-Language Support**: Parses `.py`, `.js`, `.ts`, `.md`, `.cpp`, `.java`, `.html`, and `.css` files.
- **Semantic Search**: Uses Google Gemini Embeddings and FAISS Vector Database to perform lightning-fast semantic search over thousands of lines of code.
- **Session Memory**: Uses Streamlit `session_state` to persist the AI model and database in memory without needing to write to the hard drive.

## 🛠️ Technologies Used
- **Frontend**: Streamlit
- **AI Framework**: LangChain (LCEL)
- **LLM & Embeddings**: Google Gemini (`gemini-2.5-flash`, `gemini-embedding-2`)
- **Vector Database**: FAISS

## 📋 Prerequisites
To run this project locally, you will need:
1. Python installed on your machine.
2. A free [Google Gemini API Key](https://aistudio.google.com/app/apikey).

## 💻 How to Run Locally

1. **Clone this repository** to your local machine.
2. **Install the required packages:**
   ```bash
   pip install -r requirements.txt
   ```
3. **Set up your API Key:**
   Create a file named `.env` in the root folder and add your Gemini API key:
   ```env
   GOOGLE_API_KEY="your-api-key-here"
   ```
4. **Run the Streamlit App:**
   ```bash
   streamlit run app.py
   ```
5. **Chat!**
   Open the Local URL provided in your terminal, paste a GitHub link into the sidebar, click Load, and start asking questions!
