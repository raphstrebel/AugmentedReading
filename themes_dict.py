from bs4 import BeautifulSoup as bs
import requests as rq
from matplotlib import colors as rgba_colors
import numpy as np

def get_color(text):
    colors_to_count, mood_to_count = colors_count(text)
    
    if mood_to_count['light'] + mood_to_count['dark'] > 0:
        mood_ratio = mood_to_count['light']/(mood_to_count['light'] + mood_to_count['dark'])
    else:
        mood_ratio = 0.5
    
    final_color = np.zeros(4)
    total = 0
    
    for color, count in colors_to_count.items():
        final_color += np.array(rgba_colors.to_rgba(color))
        total += 1
    
    if total > 0:
        final_color /= total
    else:
        final_color = [1,1,1,1]
        
    final_color[3] = mood_ratio
    
    return final_color

def get_colors_from_text(text):
    themes = get_themes_from_text(text)
    colors = {}
    
    for t in themes.keys():
        if t in element_to_color.keys():
            if element_to_color[t] in colors.keys():
                colors[element_to_color[t]] += 1
            else:
                colors[element_to_color[t]] = 1
    return colors
    
def get_themes_from_text(text):
    themes_to_count = {}
    for word in text:
        if word in themes_dict.keys():
            if themes_dict[word] in themes_to_count.keys():
                themes_to_count[themes_dict[word]] += 1
            else:
                themes_to_count[themes_dict[word]] = 1
    return themes_to_count

def colors_count(cleaned_text):
    colors_to_count = {}
    mood_to_count = {'light': 0, 'dark': 0}
    for word in cleaned_text:
        
        colors_to_count = get_colors_from_text(cleaned_text)
        
        if word in colors:
            c = word
            if c in colors_to_count.keys():
                colors_to_count[c] += 1
            else:
                colors_to_count[c] = 1
        if word in mood.keys():
            m = mood[word]
            if m in mood_to_count.keys():
                mood_to_count[m] += 1
            else:
                mood_to_count[m] = 1
                
    return colors_to_count, mood_to_count

def get_dict():
    themes = ["fire", "rain", "wind", "forest","water"]
    themes_dict = {}
    for theme in themes:
        link = "https://inspirassion.com/en/related/" + theme
        req = rq.get(link)
        page = bs(req.text)
        strongs = page.find_all("strong")
        for val in strongs:
            themes_dict[val.text] = theme
    return themes_dict

colors = ['blue', 'red', 'white', 'green', 'yellow', 'orange', 'maroon', 'violet', 'gray']

mood = {'obscure' : 'dark', 'dark': 'dark', 'tenebrous':'dark', 'shadowy':'dark','crepuscular':'dark', 'sunny': 'light', 'bright': 'light', 'light': 'light', 'sun': 'light', 'cloud': 'dark', 'storm': 'dark', 'lightning': 'light'}

element_to_color = {'dragon': 'red', 'fire':'red', 'city': 'gray', 'storm':'blue', 'water':'blue', 'forest':'green', 'engine':'gray', 'blue':'blue', 'red':'red', 'white':'white', 'green':'green', 'yellow':'yellow', 'orange':'orange', 'maroon':'maroon', 'violet':'violet', 'gray':'gray'}

themes_dict = {
 'dragon': 'dragon',
 'monster': 'dragon',
 'water': 'water',
 'burn': 'fire',
 'firing': 'fire',
 'gunshots': 'fire',
 'firecrackers': 'fire',
 'spark': 'fire',
 'lighted': 'fire',
 'burning': 'fire',
 'fire': 'fire',
 'flames': 'fire',
 'lit': 'fire',
 'Firecracker': 'fire',
 'burned': 'fire',
 'sparks': 'fire',
 'light': 'fire',
 'scorched': 'fire',
 'fired': 'fire',
 'flame': 'fire',
 'storm': 'wind',
 'flamed': 'fire',
 'burnt': 'fire',
 'fiery': 'fire',
 'blaze': 'fire',
 'flaming': 'fire',
 'burns': 'fire',
 'deluge': 'rain',
 'Flood': 'rain',
 'fires': 'fire',
 'scorch': 'fire',
 'storms': 'wind',
 'torched': 'fire',
 'sandstorm': 'wind',
 'wildfire': 'fire',
 'lightning': 'storm', ###
 'sun': 'orange',
 'deluged': 'rain',
 'crackles': 'fire',
 'torches': 'fire',
 'showers': 'rain',
 'shower': 'rain',
 'sky': 'wind',
 'mist': 'rain',
 'rain': 'water',
 'rainfall': 'wind',
 'hurricane': 'storm',
 'windy': 'wind',
 'water': 'water',
 'hurricanes': 'storm',
 'stormy': 'storm', ##
 'windier': 'wind',
 'Stormy': 'wind',
 'tempest': 'wind',
 'typhoon': 'wind',
 'Tempest': 'wind',
 'rained': 'rain',
 'tornados': 'wind',
 'raining': 'rain',
 'clouds': 'wind',
 'thunderstorm': 'storm', ###
 'winds': 'wind',
 'flooding': 'rain',
 'floods': 'rain',
 'seawater': 'water',
 'rainy': 'rain',
 'cyclone': 'wind',
 'mists': 'rain',
 'tornado': 'wind',
 'thunderstorms': 'storm', ##
 'wind': 'wind',
 'breeze': 'wind',
 'thunder': 'storm', ###
 'misty': 'rain',
 'foggy': 'rain',
 'sail': 'wind',
 'ocean': 'water',
 'sails': 'wind',
 'vegetation': 'forest',
 'hill': 'forest',
 'lands': 'forest',
 'hills': 'forest',
 'trails': 'forest',
 'plains': 'forest',
 'land': 'forest',
 'pine': 'forest',
 'valley': 'forest',
 'foliage': 'forest',
 'alpine': 'forest',
 'forests': 'forest',
 'trailing': 'forest',
 'plain': 'forest',
 'mountainous': 'forest',
 'coral': 'forest',
 'Valley': 'forest',
 'rainforest': 'forest',
 'wild': 'forest',
 'Alpine': 'forest',
 'Forest': 'forest',
 'summit': 'forest',
 'valleys': 'forest',
 'woodland': 'forest',
 'oak': 'forest',
 'sapling': 'forest',
 'willow': 'forest',
 'plantations': 'forest',
 'tropical': 'forest',
 'countryside': 'forest',
 'tree': 'forest',
 'rainforests': 'forest',
 'walnut': 'forest',
 'prairie': 'forest',
 'woods': 'forest',
 'swamps': 'forest',
 'trees': 'forest',
 'lake': 'water',
 'park': 'forest',
 'coast': 'water',
 'lake': 'water',
 'hell': 'fire',
 'landscape': 'forest',
 'inland': 'forest',
 'lakes': 'water',
 'Woodland': 'forest',
 'Oaks': 'forest',
 'willows': 'forest',
 'rivers': 'water',
 'parks': 'forest',
 'deserts': 'forest',
 'desert': 'forest',
 'nature': 'forest',
 'mountains': 'forest',
 'grassy': 'forest',
 'forest': 'forest',
 'Prairies': 'forest',
 'Woods': 'forest',
 'wilderness': 'forest',
 'glaciers': 'water',
 'swamp': 'forest',
 'jungles': 'forest',
 'Lake': 'water',
 'Park': 'forest',
 'natures': 'forest',
 'mountain': 'forest',
 'landscapes': 'forest',
 'gardens': 'forest',
 'fauna': 'forest',
 'river': 'water',
 'parcel': 'forest',
 'wildlife': 'forest',
 'glacial': 'water',
 'grass': 'forest',
 'Glacier': 'water',
 'jungle': 'forest',
 'aquatic': 'water',
 'sea': 'water',
 'ponds': 'water',
 'waters': 'water',
 'pool': 'water',
 'swimming': 'water',
 'immersed': 'water',
 'gutter': 'water',
 'saunas': 'water',
 'soak': 'water',
 'wash': 'water',
 'flammable': 'fire',
 'flow': 'water',
 'bathwater': 'water',
 'car': 'engine',
 'taxi': 'city',
 'crowd': 'city',
 'bus': 'engine',
 'transport': 'engine',
 'tramway': 'city',
 'metro': 'city',
 'plane': 'engine',
 'engine': 'engine',
 'bike': 'engine'
}
