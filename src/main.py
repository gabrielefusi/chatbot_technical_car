import os
from dotenv import load_dotenv
from langchain import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain.schema.runnable import RunnablePassthrough

from src.load_data import load_car_docs
from src.embed_store import create_embedding_and_store
from src.retriever.py import create_retriever

load_dotenv()

# Load API key
openai_api_key = os.getenv("OPENAI_API_KEY")
if not openai_api_key:
    raise ValueError("OpenAI API key not found! Check your .env file.")

# Step 1: Load documents
docs = load_car_docs("data/mg-zs-warning-messages.html")

# Step 2: Embed and store documents
vector_store = create_embedding_and_store(docs, persist_directory="db")

# Step 3: Create a retriever
retriever = create_retriever(vector_store)

# Step 4: Define LLM and prompt template
model = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)
prompt = PromptTemplate(
    input_variables=["context", "question"],
    template="You are a car assistant. Based on the following context, answer the question.\n\nContext: {context}\n\nQuestion: {question}"
)

# Step 5: Define RAG chain
rag_chain = ({"context": retriever, "question": RunnablePassthrough()} | prompt | model)

# Step 6: Invoke RAG chain with a sample query
query = "What does the Cruise Control Fault mean?"
result = rag_chain.invoke({"question": query})
print("Response:", result)
