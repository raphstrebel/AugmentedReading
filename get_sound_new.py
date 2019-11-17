def get_sound(theme_freq):
    sound_freq = {}
    
    for theme, freq in theme_freq.items():
        if theme not in theme_to_sound.keys():
            continue
            
        sound = theme_to_sound[theme]
        
        if sound == '':
            continue
        
        if sound in sound_freq.keys():
            sound_freq[sound] += freq
        else:
            sound_freq[sound] = freq
    
    if len(sound_freq) == 0:
        return ''
    
    return max(sound_freq, key=lambda x: sound_freq[x])
            

theme_to_sound = {
 'dragon': 'dragon_shout',
 'fire': 'calm_fire',
 'city': 'city',
 'storm': 'thunder_rain',
 'water': 'light_rain',
 'forest': 'calm_forest',
 'engine': '',
 'blue': '',
 'red': '',
 'white': '',
 'green': '',
 'yellow': '',
 'orange': '',
 'maroon': '',
 'violet': '',
 'gray': '',
 'gold': '',
 'cold': 'cold',
 'rain': 'rainy_storm',
 'ocean': 'seagulls',
 'lightning': 'thunder',
 'wind': 'thunder_rain'
}

