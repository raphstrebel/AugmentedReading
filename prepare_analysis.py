from emotions import get_emotions_from_keywords, best_emotion
from keywords_extraction import get_keywords_from_text
from themes_dict import get_color_and_theme, themes_dict

def get_all_parameters(text):
    keywords = get_keywords_from_text(text)
    
    emotions = get_emotions_from_keywords(keywords)
    single_emotion = best_emotion(emotions)
    
    color, theme = get_color_and_theme(keywords)
    
    print(theme)
    single_theme = max(k for k, v in theme.items() if v != 0)
    
    return color, single_emotion, single_theme


def get_music(arg):
    return arg[1]

def get_sound(arg):
    return arg[2]

def get_color(arg):
    return arg[0]