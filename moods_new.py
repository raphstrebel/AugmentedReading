import pandas as pd

word_emotion = pd.read_csv("emotion_db.csv")
word_emotion = word_emotion.drop(columns=["anticipation", "surprise", "trust", "disgust", "positive", "negative"])

def get_music(words):
    nAnger = 0
    nJoy = 0
    nFear = 0
    nSadness = 0
    for w in words:
        row = word_emotion[word_emotion.word==w]
        print(row)
        if len(row) > 0:
            nAnger += row["anger"].values[0]
            nJoy += row["joy"].values[0]
            nSadness += row["sadness"].values[0]
            nFear += row["fear"].values[0]
        print(nAnger, nJoy, nFear, nSadness)

    return highest_emotion(nAnger, nJoy, nFear, nSadness)
            
def highest_emotion(nAnger, nJoy, nFear, nSadness):
    labels = ["anger", "joy", "fear", "sadness"]
    counts = [nAnger, nJoy, nFear, nSadness]
    
    for i in range(4):
        if counts[i] == max(counts):
            return labels[i]