import pandas as pd

def get_emotions_from_keywords(keywords):

    word_emotion = pd.read_csv("emotion_db.csv")
    word_emotion = word_emotion.drop(columns=["anticipation", "surprise", "trust"])

    keywords_df = pd.DataFrame(keywords, columns= ["word"], dtype="str")
    keywords_emotion = word_emotion.merge(keywords_df, on="word").drop(columns="word")
    
    return keywords_emotion.sum(axis=0).to_dict()
    