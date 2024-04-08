from src.search.preprocess import stem_words


def text_match(word: str, text: str) -> bool:
    return word in text


def evaluate_query(query: str, response: str):
    satisfy = False
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

    print(words)
    
    print('Response: ', response)
    for word in words:
        query = query.replace(word, str(text_match(word, response)))

    for delim in list(delimiters.keys()):
        query = query.replace(delim, delimiters[delim])
    
    print('Query: ', query)

    try:
        satisfy = eval(query)
        print('Result: ', satisfy)
    except Exception:
        satisfy = False
    
    print('Verdict: ', satisfy)
    print('-' * 50)
    
    return satisfy
    