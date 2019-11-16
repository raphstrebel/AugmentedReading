import nltk
from nltk.tokenize import RegexpTokenizer
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.stem.porter import PorterStemmer

import rake_nltk
from rake_nltk import Rake

nltk.download('wordnet')

from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize 

def get_keywords_from_text(text):
    stop_words = set(stopwords.words('english')) 
    word_tokens = word_tokenize(text.lower()) 

    filtered_sentence = [w for w in word_tokens if not w in stop_words] 

    tokenizer = RegexpTokenizer(r'\w+')  
    lemmatizer = WordNetLemmatizer()
    
    keywords = []

    for w in filtered_sentence:
        word_tok = tokenizer.tokenize(w)
        for w_t in word_tok:
            keywords.append(lemmatizer.lemmatize(w_t, "v"))

    return keywords

def get_keywords_from_text_depr(text):
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