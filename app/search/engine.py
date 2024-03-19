from typing import List
from rank_bm25 import BM25Okapi


class Searcher:
    def __init__(self, corpus: List[str], tokenized_corpus: List[str]):
        self.corpus = corpus
        self.bm25 = BM25Okapi([doc.split(' ') for doc in tokenized_corpus])

    def make_search(self, tokenized_query: str, k: int):
        return self.bm25.get_top_n(tokenized_query, self.corpus, n=k)
    