import sys
sys.path.append("..")

from typing import List
from pathlib import Path

from langchain_community.document_loaders import UnstructuredFileLoader
from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter
from unstructured.cleaners.core import clean_extra_whitespace, clean_non_ascii_chars

from config import config


def load_files(path: Path) -> List[Document]:
    files = list(p.resolve() for p in Path(path).glob("**/*") if p.suffix in config.ALLOWED_FILES_FORMAT)

    loader = UnstructuredFileLoader(
        files,
        loader_kwargs=config.TEXT_LOADER_KWARGS,
        post_processors=[clean_extra_whitespace])
    docs = loader.load()

    return docs


def split_docs(docs: List[Document]) -> List[Document]:
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=config.CHUNK_SIZE, 
        chunk_overlap=config.CHUNK_OVERLAP)
    
    return text_splitter.split_documents(docs)
    