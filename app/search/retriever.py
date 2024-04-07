import sys
sys.path.append("..")

import streamlit as st
from langchain_community.retrievers import BM25Retriever

from search.loader import load_files, split_docs
from config import config


@st.cache_resource
def setup_retriever(filenames):
    docs = load_files(filenames)
    splits = split_docs(docs)

    retriever = BM25Retriever.from_documents(splits)
    retriever.k = config.K_TO_RETRIEVE

    return retriever
