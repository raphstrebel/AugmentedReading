import pandas as pd

word_emotion = pd.read_csv("emotion_db.csv")
word_emotion = word_emotion.drop(columns=["anticipation", "surprise", "trust", "disgust", "positive", "negative"])

def get_music(words):
    keywords_df = pd.DataFrame(words, columns= ["word"], dtype="str")
    keywords_emotion = word_emotion.merge(keywords_df, on="word").drop(columns="word")
    
    emotions_to_val = keywords_emotion.sum(axis=0).to_dict()
    
    nAnger = emotions_to_val['anger']
    nJoy = emotions_to_val['joy']
    nFear = emotions_to_val['fear']
    nSadness = emotions_to_val['sadness']

    return highest_emotion(nAnger, nJoy, nFear, nSadness)
            
def highest_emotion(nAnger, nJoy, nFear, nSadness):
    labels = ["anger", "joy", "fear", "sadness"]
    counts = [nAnger, nJoy, nFear, nSadness]
    
    m = max(counts)
    
    if m == 0:
        return ''
    
    for i in range(4):
        if counts[i] == m:
            return labels[i]