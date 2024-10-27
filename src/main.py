# Set your API key to a variable
import os
openai_api_key = os.environ["OpenAi1"]

# Import the required packages
import langchain
from langchain import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain.document_loaders import UnstructuredHTMLLoader
from langchain_openai import OpenAIEmbeddings
from langchain.schema.runnable import RunnablePassthrough
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import Chroma
from langchain_community.document_loaders import UnstructuredHTMLLoader

# Load the HTML as a LangChain document loader
loader = UnstructuredHTMLLoader(file_path="data/mg-zs-warning-messages.html")
car_docs = loader.load()

# Initialize RecursiveCharacterTextSplitter to make chunks of HTML text
text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)

# Split GDPR HTML
splits = text_splitter.split_documents(car_docs)

# Initialize Chroma vectorstore with documents as splits and using OpenAIEmbeddings
vectorstore = Chroma.from_documents(documents=splits, embedding=OpenAIEmbeddings(openai_api_key=openai_api_key))

# Setup vectorstore as retriever
retriever = vectorstore.as_retriever()

# Define RAG prompt
prompt = PromptTemplate(input_variables=['question', 'context'], template="You are an assistant for question-answering tasks. Use the following pieces of retrieved context to answer the question. If you don't know the answer, just say that you don't know. Use three sentences maximum and keep the answer concise.\nQuestion: {question} \nContext: {context} \nAnswer:")

# Initialize chat-based LLM with 0 temperature and using GPT-3.5 Turbo
model = ChatOpenAI(openai_api_key=openai_api_key, model_name="gpt-3.5-turbo", temperature=0)

# Setup the chain
rag_chain = (
    {"context": retriever , "question": RunnablePassthrough()}
    | prompt
    | model
)

# Initialize query
query = "The Gasoline Particular Filter Full warning has appeared. What does this mean and what should I do about it?"

# Invoke the query
answer = rag_chain.invoke(query).content
print(answer)
