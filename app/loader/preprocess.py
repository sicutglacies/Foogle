import string
from typing import List


def to_lowercase(txts: List[str]) -> List[str]:
    return list(map(lambda x: str.lower(x), txts))


def remove_punctuation(txts: List[str]) -> List[str]:
    return list(map(lambda x: x
        .translate(
            str.maketrans('', '', string.punctuation)), txts))