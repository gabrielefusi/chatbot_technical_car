def create_retriever(vector_store):
    """Create a retriever from the ChromaDB vector store."""
    return vector_store.as_retriever()
