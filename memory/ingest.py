"""This is the logic for ingesting data into LangChain."""
from langchain.vectorstores import Chroma
from langchain.embeddings.openai import OpenAIEmbeddings
from pathlib import Path
from langchain.text_splitter import CharacterTextSplitter
from langchain.document_loaders import TextLoader
import time 
from utils import config_util as cfg
openai_api_key = cfg.key_chatgpt_api_key

def ingest(memory_path="raw_memory/lsc.txt", database_path="./"):
# Here we load in the data in the format that Notion exports it in.
    embedding = OpenAIEmbeddings(openai_api_key=openai_api_key)

    loader = TextLoader(memory_path) # source
    documents = loader.load()
    # Here we split the documents, as needed, into smaller chunks.
    # We do this due to the context limits of the LLMs.
    text_splitter = CharacterTextSplitter(chunk_size=500, separator="\n")
    docs = text_splitter.split_documents(documents)
    persist_directory=database_path
    print("Start to ingest!")
    start_time = time.time()
    db = Chroma.from_documents(documents=docs, embedding=embedding, persist_directory=persist_directory)
    print(f"Ingestion complete!, time cost: {time.time() - start_time} seconds.")
    db.persist()

if __name__ == "__main__":
    
    ingest()