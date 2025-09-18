# app.py

import os
from dotenv import load_dotenv
import streamlit as st
from langchain.document_loaders import PyPDFLoader, Docx2txtLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import Chroma
from langchain.chat_models import ChatOpenAI
from langchain.chains import RetrievalQA

# Load OpenAI API key from .env file
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

st.set_page_config(page_title="Document QA System", layout="centered")
st.title("📄 Document-based Question Answering System (GenAI)")

# Upload PDF or DOCX file
uploaded_file = st.file_uploader("Upload PDF or DOCX", type=["pdf", "docx"])
persist_directory = "chroma_db"

if uploaded_file:
    # Save file temporarily
    temp_path = "temp_file"
    with open(temp_path, "wb") as f:
        f.write(uploaded_file.read())

    # Load document
    if uploaded_file.name.lower().endswith(".pdf"):
        loader = PyPDFLoader(temp_path)
    else:
        loader = Docx2txtLoader(temp_path)
    documents = loader.load()

    # Split into chunks
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    docs = text_splitter.split_documents(documents)

    # Create embeddings & vector store
    embeddings = OpenAIEmbeddings(openai_api_key=OPENAI_API_KEY)
    vectorstore = Chroma.from_documents(docs, embeddings, persist_directory=persist_directory)
    vectorstore.persist()

    # Create QA system
    llm = ChatOpenAI(model="gpt-4", temperature=0, openai_api_key=OPENAI_API_KEY)
    qa = RetrievalQA.from_chain_type(llm=llm, chain_type="stuff", retriever=vectorstore.as_retriever())

    # Ask question
    query = st.text_input("Ask a question about the document:")
    if query:
        answer = qa.run(query)
        st.subheader("Answer:")
        st.write(answer)
