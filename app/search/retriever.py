import sys
sys.path.append("..")

import streamlit as st
from langchain_community.retrievers import BM25Retriever

from search.loader import load_files, split_docs
from search.preprocess import preprocess_text
from config import config


@st.cache_resource(show_spinner = False)
def setup_retriever(filenames):
    docs = load_files(filenames)
    splits = split_docs(docs)
    for split in splits:
        split.metadata['original_text'] = split.page_content
        split.page_content = preprocess_text(split.page_content)

    retriever = BM25Retriever.from_documents(splits)
    retriever.k = config.K_TO_RETRIEVE

    return retriever
