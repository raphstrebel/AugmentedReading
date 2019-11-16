import nltk
from nltk import sentiment as st
from matplotlib import pyplot as plt
import pandas as pd
import numpy as np
db = pd.read_csv("NRC-Emotion-Lexicon-Wordlevel-v0.92.txt", sep = "\t", header = None)
unique_words = pd.DataFrame(unique_words)
vals = np.zeros([len(unique_words), 10])
for it, word in enumerate(db[0].unique()):
    vals[it] = db[2][db[0] == word]
vals = pd.DataFrame(vals)    
empty_db = pd.concat([unique_words, vals], axis = 1, ignore_index=True)
empty_db.rename({0:"word", 1: "anger", 2: "anticipation", 3 : "disgust", 4: "fear", 5:"joy", 6:"negative", 7:"positive", 8:"sadness", 9:"surprise", 10:"trust"}, axis = "columns")