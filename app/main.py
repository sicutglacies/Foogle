import streamlit as st
from langchain.retrievers.bm25 import default_preprocessing_func

from search.loader import get_filenames
from search.retriever import setup_retriever
from web.generator import response_generator
from config import config


st.set_page_config(page_title="Search")
st.title("BM25 Search")
st.header("Поисковик по каталогу")


filenames = get_filenames(config.FILES_PATH)
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
    st.session_state.messages.append({"role": "user", "content": prompt})

    with st.chat_message("assistant"):
        query = st.session_state.messages[-1]['content']
        results = retriever.get_relevant_documents(query)
        scores = sorted(retriever.vectorizer.get_scores(default_preprocessing_func(query)))[::-1][:config.K_TO_RETRIEVE]

        response = st.write_stream(response_generator(scores, results))

    st.session_state.messages.append({"role": "assistant", "content": response})
        