import os
from langchain_community.document_loaders import PyPDFLoader, PyMuPDFLoader
import numpy as np
from sentence_transformers import SentenceTransformer
import chromadb
from chromadb.config import Settings
import uuid
from typing import List, Dict, Any, Tuple
from sklearn.metrics.pairwise import cosine_similarity
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.messages import HumanMessage, SystemMessage
from pathlib import Path
from parsing import *
from embeddings import *
from retrieving import *
from vectordbstore import *

# INGESTION STEPS
# Read PDF Docs

def loading_pdfs(pdf_dir):

    file_list = [os.path.join(pdf_dir, i) for i in (os.listdir('Data'))]
    print(f'Found {len(file_list)} files to process.......')

    

    return file_list

pdf_dir = 'Data'
loading_pdfs(pdf_dir)

# Chunking 



# Embedding



# Store in vector DB



# RETRIEVE STEPS
# Define & Load LLM




# Prompt embedding



# Query from vector DB



# Prompting & output




