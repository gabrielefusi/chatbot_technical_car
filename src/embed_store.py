from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings

def create_embedding_and_store(docs, persist_directory="db"):
    """Split documents, create embeddings, and store in ChromaDB."""
    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    doc_chunks = splitter.split_documents(docs)

    embeddings = OpenAIEmbeddings()
    vector_store = Chroma.from_documents(documents=doc_chunks, embedding=embeddings, persist_directory=persist_directory)
    return vector_store
