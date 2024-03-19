from pathlib import Path
from loader.loader import load_files, split_files
from loader.preprocess import to_lowercase, remove_punctuation
from search.engine import Searcher


N_SENT_TO_RETRIEVE = 3
TXT_DIR = Path('/Users/sicutglacies/Documents/University/python/Foogle/data')

docs = load_files(TXT_DIR)
docs_sentences = split_files(docs)


tk_corpus = to_lowercase(docs_sentences)
tk_corpus = remove_punctuation(tk_corpus)

searcher = Searcher(docs_sentences, tk_corpus)


if __name__ == "__main__":
    while True:
        query = input("Enter your search query: ").lower().split(" ")
        resutls = searcher.make_search(query, N_SENT_TO_RETRIEVE)
        scores = sorted(searcher.bm25.get_scores(query))[::-1][:N_SENT_TO_RETRIEVE]
        for n, (res, score) in enumerate(zip(resutls, scores)):
            print(f'{n+1}. /{round(score, 2)}/ {res}')
    
    
    