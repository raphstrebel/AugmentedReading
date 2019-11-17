import numpy as np
from matplotlib import colors as rgba_colors

def get_color(theme_freq):
    color_to_count = {}
    for theme in theme_freq.keys():
        if not theme in themes_to_color.keys():
            continue
        
        color = themes_to_color[theme]
        if color in color_to_count.keys():
            color_to_count[color] += theme_freq[theme]
        else:
            color_to_count[color] = theme_freq[theme]
   
    final_color = np.zeros(4)
    
    total = 0
    for color, count in color_to_count.items():
        final_color += np.array(rgba_colors.to_rgba(color)) * count
        total += count
    
    if total > 0:
        final_color /= total
    else:
        final_color = [1,1,1,1]
        
    final_color[3] = 1
    
    return final_color
    
themes_to_color = {'dragon': 'red', 'fire': 'red', 'city': 'gray', 'storm':'blue', 'water':'blue', 'forest':'green', 'engine':'gray', 'blue':'blue', 'red':'red', 'white':'white', 'green':'green', 'yellow':'yellow', 'orange':'orange', 'maroon':'maroon', 'violet':'violet', 'gray':'gray', 'cold':'white', 'rain':'blue', 'ocean':'blue', 'lightning':'white', 'wind':'gray', 'gold':'yellow'}