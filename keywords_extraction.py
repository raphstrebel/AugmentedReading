import nltk
from nltk.tokenize import RegexpTokenizer
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.stem.porter import PorterStemmer

import rake_nltk
from rake_nltk import Rake

nltk.download('wordnet')

def get_keywords_from_text(text):
    r = Rake()
    r.extract_keywords_from_text(text)
    keywords = r.get_ranked_phrases()
    
    lemmatizer = WordNetLemmatizer()
    tokenizer = RegexpTokenizer(r'\w+')
    stemming = PorterStemmer()

    cleaned_keywords = set()
    #all_keywords = set()

    for k in keywords:

        k_tok = tokenizer.tokenize(k)

        for k_t in k_tok:
            k_lem = lemmatizer.lemmatize(k_t, "v")    
            #k_stem = stemming.stem(k_t)

            #if k_lem != k_stem:
            #    all_keywords.add(k_stem)

            cleaned_keywords.add(k_lem)
            #all_keywords.add(k_lem)
    return cleaned_keywords