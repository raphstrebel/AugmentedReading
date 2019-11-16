import requests
import json
import colorsys

MAX_HUE = 65535
MAX_SATURATION = 254
MAX_BRIGHTNESS = 254

USERNAME = "-zCbH7c4lBICY37ZyPPu9h-s7NFzckHHcd9uQCju"
IP_ADDR = "192.168.1.2"
LAMP_ID = "1"

STATE_URL = "http://"+IP_ADDR+"/api/"+USERNAME+"/lights/"+LAMP_ID+"/state"

def displayNewColor(r, g, b, brightness=1):
    """
    Changes the color of the lamp.

    args:
        r, g, b (floats): RGB colors in the range 0-1 (e.g. red = 1,0,0)
        saturation (float): saturation in the range 0-1
        brightness (float): brightness in the range 0-1
    returns:
        JSON response from the Hue device
    """

    h, s, v = colorsys.rgb_to_hsv(r,g,b)
    print(h)
    hue = int(h * MAX_HUE)
    saturation = s

    body = {"on":True, "sat":int(saturation * MAX_SATURATION), "bri":int(brightness * MAX_BRIGHTNESS), "hue": hue}
    print(body)
    
    return requests.put(STATE_URL, data=json.dumps(body))
