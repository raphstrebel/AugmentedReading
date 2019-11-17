import nltk
from nltk.tokenize import RegexpTokenizer
from nltk.stem.wordnet import WordNetLemmatizer

import string

#nltk.download('wordnet')

from nltk.corpus import stopwords 

def sanitize(text):
    stop_words = set(stopwords.words('english')) 
    text = text.lower().split(" ")

    text_without_stop_words = [w for w in text if (not w in stop_words) and (not w in string.punctuation)] 

    tokenizer = RegexpTokenizer(r'\w+')  
    lemmatizer = WordNetLemmatizer()
    
    keywords = []

    for w in text_without_stop_words:
        word_tok = tokenizer.tokenize(w)
        for w_t in word_tok:
            if len(w_t) > 1:
                keywords.append(lemmatizer.lemmatize(w_t, "v"))

    return keywords