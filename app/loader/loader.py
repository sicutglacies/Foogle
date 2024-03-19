from typing import List
from pathlib import Path

# from nltk import sent_tokenizer


def load_files(path: Path) -> List[str]:
    print('Loading files...')
    docs = []
    for p in path.glob('*.txt'):
        with open(p) as f:
            content = f.read()
        docs.append(content)
    return docs


def flatten_comprehension(ll):
    return [item for row in ll for item in row]


def split_files(txts: List[str]) -> List[str]:
    sentences = flatten_comprehension(list(map(lambda x: x.split('.'), txts)))
    filtered_sentences = list(filter(None, sentences))
    return list(map(lambda x: x.replace('\n', ''), filtered_sentences))
    