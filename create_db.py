import os
import pickle

from langchain import FAISS
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter

from langchain.document_loaders import DirectoryLoader, TextLoader

from dotenv import load_dotenv

loader = DirectoryLoader(
    path="static",
    glob="**/*.json",
    show_progress=True,
    loader_cls=TextLoader,
    loader_kwargs={"encoding": "utf-8"},
)

load_dotenv()

OPEN_API_KEY = os.getenv("OPEN_API_KEY")

docs = loader.load()
char_text_spliter = RecursiveCharacterTextSplitter(
    chunk_size=1000, chunk_overlap=0
)
document = char_text_spliter.split_documents(docs)
persist_directory = "db"
open_ai_embedding = OpenAIEmbeddings(openai_api_key=OPEN_API_KEY)
vstore = FAISS.from_documents(document, open_ai_embedding)
with open("faiss_store_openai.pkl", "wb") as file:
    pickle.dump(vstore, file)
