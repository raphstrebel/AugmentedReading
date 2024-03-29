import pandas as pd

emotion_to_music = {'anger': 'angry',
 'disgust': '',
 'fear': 'fear',
 'joy': 'happy',
 'negative': '',
 'positive': '',
 'sadness': 'sad'
}

def get_emotions_from_keywords(keywords):

    word_emotion = pd.read_csv("emotion_db.csv")
    word_emotion = word_emotion.drop(columns=["anticipation", "surprise", "trust", "disgust", "positive", "negative"])

    keywords_df = pd.DataFrame(keywords, columns= ["word"], dtype="str")
    keywords_emotion = word_emotion.merge(keywords_df, on="word").drop(columns="word")
    
    return keywords_emotion.sum(axis=0).to_dict()

def best_emotion(emotions):
    negative_emotions = [(emotion, count) for emotion, count in emotions.items() if emotion not in ["joy", "positive", "negative"]]
    
    if sum(emotions.values()) == 0:
        return None

    if (emotions["positive"] > emotions["negative"] and emotions["joy"] >= max(negative_emotions, key=lambda x: x[1])[1]):
        return "joy"
    else:
        return max(negative_emotions, key=lambda x: x[1])[0]