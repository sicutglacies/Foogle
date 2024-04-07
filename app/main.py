from langchain_community.retrievers import BM25Retriever
from langchain.retrievers.bm25 import default_preprocessing_func

from loader.loader import load_files, split_docs
from config import config


docs = load_files(config.FILES_PATH)
splits = split_docs(docs)

retriever = BM25Retriever.from_documents(splits)
retriever.k = config.K_TO_RETRIEVE


if __name__ == "__main__":
    print("Ready to work")
    while True:
        query = input("Enter your search query: ")
        results = retriever.get_relevant_documents(query)
        scores = sorted(retriever.vectorizer.get_scores(default_preprocessing_func(query)))[::-1][:config.K_TO_RETRIEVE]
        for n, (res, score) in enumerate(zip(results, scores)):
            print(n, score, res.page_content)
            print('-' * 50)
