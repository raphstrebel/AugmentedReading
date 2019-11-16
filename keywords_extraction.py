import nltk
from nltk.tokenize import RegexpTokenizer
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.stem.porter import PorterStemmer

import rake_nltk
from rake_nltk import Rake
import string

nltk.download('wordnet')

from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize

def get_keywords_from_text(text):
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

def get_keywords_from_text_other(text):
    stop_words = set(stopwords.words('english')) 
    word_tokens = word_tokenize(text.lower()) 
    
    print(word_tokens)

    filtered_sentence = [w for w in word_tokens if not w in stop_words] 
    
    print(filtered_sentence)

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