import re 
import string

from nltk import word_tokenize
from nltk.corpus import stopwords
from nltk.stem.snowball import SnowballStemmer


stop = set(stopwords.words('english')).union(set(stopwords.words('russian')))
eng_stemmer = SnowballStemmer("english")
rus_stemmer = SnowballStemmer('russian')


def has_cyrillic(text):
    return bool(re.search('[а-яА-Я]', text))


def stem_words(words):
    return ' '.join([rus_stemmer.stem(plural) if has_cyrillic(plural) else eng_stemmer.stem(plural) for plural in words])


def preprocess_text(text):
    # Lowercase the text
    text = text.lower()
    # Remove punctuation
    text = text.translate(str.maketrans('', '', string.punctuation))
    text_without_stop = [x for x in word_tokenize(text) if x not in stop]
    stemmed_text = stem_words(text_without_stop)
    
    return stemmed_text
    