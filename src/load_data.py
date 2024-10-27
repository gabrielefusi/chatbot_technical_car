import os
from dotenv import load_dotenv
from langchain.document_loaders import UnstructuredHTMLLoader

load_dotenv()  # Load environment variables from .env file

def load_car_docs(file_path):
    """Load car documents from HTML file."""
    loader = UnstructuredHTMLLoader(file_path=file_path)
    return loader.load()
