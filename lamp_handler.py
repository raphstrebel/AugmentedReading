import requests
import json
import colorsys
import time
from threading import Thread

MAX_HUE = 65535
MAX_SATURATION = 254
MAX_BRIGHTNESS = 254

USERNAME = "-zCbH7c4lBICY37ZyPPu9h-s7NFzckHHcd9uQCju"
IP_ADDR = "192.168.1.2"
LAMP_ID = "1"

STATE_URL = "http://"+IP_ADDR+"/api/"+USERNAME+"/lights/"+LAMP_ID+"/state"

def switch_light(on):
    """
    Switches the light on (True) of off (False)

    args:
        on (boolean)
    """

    body = {"on":on}
    
    return requests.put(STATE_URL, data=json.dumps(body))

def display_new_color(r, g, b, brightness=1):
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

def party_mode_wrapped():
    for i in range(5):
        if i%2 == 0:
            display_new_color(1, 0, 0)
        if i%2 == 1:
            display_new_color(0, 1, 0)
        time.sleep(1)

def party_mode():
    t = Thread(target=party_mode_wrapped)
    t.start()
