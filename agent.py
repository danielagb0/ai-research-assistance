# agent.py
import os
from dotenv import load_dotenv

load_dotenv()

from openai import OpenAI
from langchain.embeddings import OpenAIEmbeddings
from langchain.llms import OpenAI as LCOpenAI
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chains import RetrievalQA
from langchain.vectorstores import FAISS
import pandas as pd


# ==========================
# ENVIRONMENT VARIABLES
# ==========================
API_KEY = os.getenv("API_KEY")
BASE_URL = os.getenv("BASE_URL", "https://api.groq.com/openai/v1")
MODEL = os.getenv("MODEL", "llama3-8b-8192")


# ==========================
# CLIENTE OPENAI-COMPATIBLE (GROQ)
# ==========================
client = OpenAI(
    api_key=API_KEY,
    base_url=BASE_URL
)


# ==========================
# LOAD DATA
# ==========================
def load_csv_to_docs(csv_path):
    df = pd.read_csv(csv_path)

    # Convertimos cada fila en un documento de texto
    docs = []
    for _, row in df.iterrows():
        text = " | ".join([f"{col}: {row[col]}" for col in df.columns])
        docs.append(text)

    return docs


# ==========================
# CHUNKING
# ==========================
def chunk_texts(texts):
    splitter = RecursiveCharacterTextSplit
