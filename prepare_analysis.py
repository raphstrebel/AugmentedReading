from emotions import get_emotions_from_keywords, best_emotion, emotion_to_music
from keywords_extraction import get_keywords_from_text
from themes_dict import get_color_and_theme, themes_dict, theme_to_music

def get_all_parameters(text):
    keywords = get_keywords_from_text(text)
    
    emotions = get_emotions_from_keywords(keywords)
    single_emotion = best_emotion(emotions)
    
    color, theme = get_color_and_theme(keywords)
    
    if len(theme.keys()) > 0: 
        single_theme = max(k for k, v in theme.items() if v != 0)
    else:
        single_theme = None
    
    return color, single_emotion, single_theme


def get_music(arg):
    emotion = arg[1]
    return emotion_to_music[emotion]

def get_sound(arg):
    theme = arg[2]
    return theme_to_music[theme]

def get_color(arg):
    return arg[0]