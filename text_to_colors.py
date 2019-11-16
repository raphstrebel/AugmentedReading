import pandas as pd
import themes_dict
from themes_dict import get_color
from keywords_extraction import get_keywords_from_text


def text_to_colors_and_emotions(text):
    keywords = get_keywords_from_text(text)
    
    ############# EMOTIONS
    word_emotion = pd.read_csv("emotion_db.csv")
    word_emotion = word_emotion.drop(columns=["anticipation", "surprise", "trust"])

    keywords_df = pd.DataFrame(keywords, columns= ["word"], dtype="str")
    keywords_emotion = word_emotion.merge(keywords_df, on="word").drop(columns="word")
    keywords_emotion.sum(axis=0)
    #############
    
    return get_color(keywords) # todo get_emotions(keywords)