import time

import streamlit as st
from langchain.retrievers.bm25 import default_preprocessing_func

from src.search.loader import get_filenames
from src.search.retriever import setup_retriever
from src.search.preprocess import preprocess_text
from src.web.generator import response_generator
from src.config import config


st.set_page_config(page_title="Search")
st.title("Foogle")
st.header("Поисковик по каталогу")


filenames = get_filenames(config.FILES_PATH)
if len(filenames) == 0:
    st.header('No files in the provided directory. Rerunning in 2 sec')
    time.sleep(2)
    st.rerun()
retriever = setup_retriever(filenames)


if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Задайте Ваш вопрос"):
    st.session_state.messages.append({"role": "user", "content": prompt})

    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        query = st.session_state.messages[-1]['content']
        results = retriever.get_relevant_documents(preprocess_text(query))
        scores = sorted(retriever.vectorizer.get_scores(default_preprocessing_func(preprocess_text(query))))[::-1][:config.K_TO_RETRIEVE]

        response = st.write_stream(response_generator(query, scores, results))

    st.session_state.messages.append({"role": "assistant", "content": response})
        