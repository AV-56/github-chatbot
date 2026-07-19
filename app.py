import os
import streamlit as st
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI,GoogleGenerativeAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
import tempfile
from langchain_community.document_loaders import GitLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter,Language

load_dotenv()

st.set_page_config(page_title="GitHub Repo Chatbot",
page_icon="🤖", 
layout="centered"
)

st.title("🤖 Chat with OpenAI Quickstart Repo")
st.write("Ask any question about the codebase!")
if "qa_chain" not in st.session_state:
    st.session_state.qa_chain = None

# sidebar
with st.sidebar:
    st.header("1. Load Repository")
    repo_url= st.text_input("GitHub Repo URL:",placeholder="https://github.com/...")
    branch_name=st.text_input("Branch Name:", value="main")
    if st.button("Load and process Repo"):
        if not repo_url:
            st.error("Please enter an URL first!")
        else:
            with st.spinner("Downloading Code.... This may take a while"):
                try:
                    with tempfile.TemporaryDirectory() as temp_dir:
                        loader = GitLoader(
                            clone_url=repo_url,
                            repo_path=temp_dir,
                            branch=branch_name,
                            file_filter=lambda file_path: file_path.endswith((".py", ".js", ".ts", ".md", ".cpp", ".java", ".html", ".css"))
                        )
                        documents=loader.load()
                        if len(documents)==0:
                            st.error(f"No documents found in the '{branch_name}' branch.")
                        else:
                            st.success(f"Successfully loaded {len(documents)} files")    
                            text_splitter= RecursiveCharacterTextSplitter(
                                chunk_size=1000,
                                chunk_overlap=200
                            )
                            chunks=text_splitter.split_documents(documents)

                            embeddings = GoogleGenerativeAIEmbeddings(model="gemini-embedding-2")
                            

                            db = FAISS.from_documents(chunks, embeddings)

                            llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

                            prompt = ChatPromptTemplate.from_template(
                                "You are a helpful AI assistant. Answer the user's question using ONLY the context provided below.\n\nContext: {context}\n\nQuestion: {question}"
                            )

                            retriever = db.as_retriever(search_kwargs={"k": 5})
                            
                            qa_chain = (
                                {"context": retriever, "question": RunnablePassthrough()} 
                                | prompt 
                                | llm
                            )
                            
                            st.session_state.qa_chain = qa_chain
                            st.success("✅ AI is ready! You can now ask questions.")


                except PermissionError:
                    pass  
                except Exception as e:
                    st.error(f"Error Loading Repo: {e}")



   # --- 3. MAIN CHAT INTERFACE ---
if st.session_state.qa_chain is None:
    st.info("👈 Please load a GitHub repository from the sidebar to start chatting!")
else:
    user_question = st.text_input("Ask a question about this codebase:")
    
    if st.button("Ask Bot"):
        if user_question:
            with st.spinner("Thinking... 🧠"):
                # Notice we use st.session_state.qa_chain here!
                response = st.session_state.qa_chain.invoke(user_question)
                
                st.success("Here is your answer:")
                st.markdown(response.content)
        else:
            st.warning("Please type a question first!")
