from Libs.libs import *


embedding_function = get_embeddings("openai")
from langchain.schema import Document
#from langchain_community.document_loaders import CSVLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveJsonSplitter
from langchain.schema import Document
import json
from pathlib import Path


from enum import Enum
from models.milvus import drop_collection

class VectorDB(Enum):
    CHROMA = "chroma"

class StoreName(Enum):
    personal_vs = os.getenv("PERSONAL_STORE_NAME")
    all_store = "all"
    

import traceback

def load_csv_documents(file_path, meta_data):
    try:
        
        loader = CSVLoader(file_path, encoding='utf-8')


        docs = loader.load()
        pages = [Document(page_content=doc.page_content, metadata={"about": meta_data}) for doc in docs]
        
        with open(file_path, 'r', encoding='utf-8') as f:
            reader = csv.reader(f)
            headers = next(reader)  # Skip the header row
            for row in reader:
                # Join row contents for simplicity; adjust as needed
                content = ', '.join(row)
                print(content)
        return pages
    
        
    except Exception as e:
        print("Detailed error loading CSV:")
        print(e)
        print(traceback.format_exc())
        return []

from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader

def load_pdf_documents(file_path, meta_data):
    try:
        pdf_loader = PyPDFLoader(file_path=file_path)
        docs = pdf_loader.load()        
        splitter = RecursiveCharacterTextSplitter(separators='\n')
        splitted_docs = splitter.split_documents(docs)
        return splitted_docs
    
        
    except Exception as e:
        print("Detailed error loading PDF:")
        print(e)
        print(traceback.format_exc())
        return []


def load_json_documents(file_path):
    json_docs = []
    file_path = r"./Data/formatted_data/wada_location.json"
    with open(file_path, "r", encoding='utf-8') as f:
        docs_json = json.load(f)
        splitter = RecursiveJsonSplitter(max_chunk_size=270)
        splited_json = splitter.split_json(docs_json)
        json_documents = splitter.create_documents(splited_json,)
        for i in range(len(json_documents)):
            json_docs = json_docs + [Document(page_content=json_documents[i].page_content)]
    return json_docs
    
    
    
    


def update_vector_store(vector_store, documents, collection_name):
    if vector_store == VectorDB.CHROMA:
        Chroma.from_documents(documents, embedding=embedding_function, persist_directory=f"./Chroma/{collection_name}_Chroma")
        return f"Chroma of the name {collection_name} has been updated"
    elif vector_store == VectorDB.MILVUS:
        Milvus.from_documents(
            embedding=embedding_function, 
            documents=documents,
            connection_args={"host": os.getenv("HOST"), "port": os.getenv("PORT")},
            collection_name=collection_name,
            drop_old = True
        )
        return f"Milvus of the name {collection_name} has been updated"
    else:
        return "Error in updating vector store."

import os
from dotenv import load_dotenv
load_dotenv()

def update_personal_store(vector_store):
    meta_data = """"Meta Data"""
    documents = load_pdf_documents(r'./Data/personal_cv.pdf', meta_data)
    return update_vector_store(vector_store, documents,  os.getenv("PERSONAL_STORE_NAME"))

def update_location(vector_store):

    documents = load_json_documents(r"./Data/formatted_data/wada_location.json")
    return update_vector_store(vector_store, documents, "wada_location_kmc")
