from pathlib import Path

from src.search.preprocess import stem_words
from src.config import config


def text_match(word: str, text: str) -> bool:
    return word in text


def extension_filter(query: str, response: str):
    no_mask_in_query = True

    ext = Path(response.metadata['source']).suffix

    for word in query.split():
        if word in config.ALLOWED_FILES_FORMAT:
            no_mask_in_query = False
            if word == ext:
                return True
    return no_mask_in_query


def evaluate_query(query: str, response: str):
    satisfy = False
    query = ' '.join([x for x in query.split() if x not in config.ALLOWED_FILES_FORMAT])
    words = str(query)

    delimiters = {
        "&": "and",
        "|": "or",
        "!": "not",
        "(": "(",
        ")": ")"
    }

    for delimiter in list(delimiters.keys()):
        words = "".join(words.split(delimiter))

    if words == query:
        return True

    words = words.lower().split()
    words = stem_words(words).split()
    
    query = stem_words(query.lower().split())

    for word in words:
        query = query.replace(word, str(text_match(word, response)))

    for delim in list(delimiters.keys()):
        query = query.replace(delim, delimiters[delim])

    try:
        satisfy = eval(query)
    except Exception:
        satisfy = False
    
    return satisfy
    