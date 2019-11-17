
def themes_to_count(words):
    to_ret = {}
    for w in words:
        if w not in words_to_themes.keys():
            continue
        theme = words_to_themes[w]
        if theme in to_ret.keys():
            to_ret[theme] += 1
        else:
            to_ret[theme] = 1
    return to_ret
        
words_to_themes = {
 'snow':'cold',
 'snowflake':'cold',
 'blizzard':'cold',
 'blizzards':'cold',
 'sand': 'gold',
 'rich': 'gold',
 'cold':'cold',
 'beach':'ocean',
 'sand':'ocean',
 'snowflakes':'cold',
 'dragon': 'dragon',
 'smaug': 'dragon',
 'monster': 'dragon',
 'water': 'water',
 'gold': 'gold',
 'golden': 'gold',
 'gems': 'gold',
 'gem': 'gold',
 'jewel': 'gold',
 'jewels': 'gold',
 'gunshots': 'fire',
 'lighted': 'fire',
 'fire': 'fire',
 'lava': 'fire',
 'magma': 'fire',
 'volcano': 'fire',
 'flames': 'fire',
 'light': 'fire',
 'flame': 'fire',
 'storm': 'storm',
 'flamed': 'fire',
 'flaming': 'fire',
 'deluge': 'rain',
 'flood': 'rain',
 'fires': 'fire',
 'storms': 'storm',
 'wildfire': 'fire',
 'lightning': 'lightning',###
 'sun': 'fire',
 'deluged': 'rain',
 'showers': 'rain',
 'shower': 'rain',
 'sky': 'wind',
 'mist': 'rain',
 'rain': 'water',
 'rainfall': 'water',
 'hurricane': 'storm',
 'windy': 'wind',
 'water': 'water',
 'hurricanes': 'storm',
 'windier': 'wind',
 'stormy': 'storm',
 'typhoon': 'storm',
 'tempest': 'storm',
 'rained': 'rain',
 'tornados': 'storm',
 'raining': 'rain',
 'clouds': 'wind',
 'thunderstorm': 'storm',
 'winds': 'wind',
 'flooding': 'water',
 'floods': 'water',
 'seawater': 'water',
 'rainy': 'rain',
 'cyclone': 'storm',
 'mists': 'rain',
 'tornado': 'storm',
 'wind': 'wind',
 'breeze': 'wind',
 'thunder': 'storm', ###
 'ocean': 'water',
 'vegetation': 'forest',
 'hill': 'forest',
 'lands': 'forest',
 'hills': 'forest',
 'trails': 'forest',
 'plains': 'forest',
 'tree': 'forest',
 'pine': 'forest',
 'valley': 'forest',
 'foliage': 'forest',
 'forests': 'forest',
 'trailing': 'forest',
 'mountainous': 'forest',
 'valley': 'forest',
 'rainforest': 'forest',
 'wild': 'forest',
 'forest': 'forest',
 'valleys': 'forest',
 'woodland': 'forest',
 'plantations': 'forest',
 'tropical': 'forest',
 'countryside': 'forest',
 'tree': 'forest',
 'rainforests': 'forest',
 'prairie': 'forest',
 'woods': 'forest',
 'swamps': 'forest',
 'trees': 'forest',
 'lake': 'water',
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
 'lake': 'water',
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
 'glacier': 'water',
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
 'bike': 'engine',
 'tree':'forest'
}
    