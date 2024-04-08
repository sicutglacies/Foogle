from typing import List
from pathlib import Path

import streamlit as st
from langchain_community.document_loaders import UnstructuredFileLoader
from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter
from unstructured.cleaners.core import clean_extra_whitespace

from src.config import config


def get_filenames(path: Path):
    return list(p.resolve() for p in Path(path).glob("**/*") if p.suffix in config.ALLOWED_FILES_FORMAT)


def load_files(files: List[Path]) -> List[Document]:
    documents = []

    progress_text = "Loading files... Please wait."
    bar = st.progress(0, text=progress_text)
    n_docs = len(files)

    for n, filepath in enumerate(files):
        loader = UnstructuredFileLoader(
            file_path=filepath,
            strategy='hi_res',
            mode='elements',
            loader_kwargs=config.TEXT_LOADER_KWARGS,
            post_processors=[clean_extra_whitespace])
        docs = loader.load()
        documents.extend(docs)
        bar.progress(round((n+1)/n_docs*100), text=f'{progress_text} {(n+1)}/{n_docs}')

    return documents


def split_docs(docs: List[Document]) -> List[Document]:
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=config.CHUNK_SIZE, 
        chunk_overlap=config.CHUNK_OVERLAP)
    
    return text_splitter.split_documents(docs)
    