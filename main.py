from video_capture import *
from text_extraction import *
from lamp_handler import *
from play_music import *

from get_color_new import *
from get_sound_new import *
from moods_new import *
from sanitize_new import *
from themes_new import *

#from themes_dict import *
#from text_to_colors import *
#from prepare_analysis import *

import cv2
import time

FOCUS_VALUE = 15
WINDOW_SIZE = 55
font = cv2.FONT_HERSHEY_SIMPLEX
white = (255, 255, 255)

def to_BGR(color):
	(r, g, b) = color
	hey =  (int(b * 255), int(g * 255), int(r * 255))
	print(hey)
	return hey

def display_frame(frame, words, color, iteration, music_name, sound_name):
	### hack
	cv2.imwrite('todel.png', frame)

	### second hack
	yo = cv2.imread('todel.png', cv2.IMREAD_COLOR)
	yo = cv2.resize(yo, (405, 720))
	cv2.imwrite("todel2.png", yo)
	yo2 = cv2.imread("todel2.png")

	### Oufff, we're good to go :-)
	yo2 = cv2.copyMakeBorder(yo2, 0, 0, 0, 800, cv2.BORDER_CONSTANT)

	### print color rectangle
	cv2.rectangle(yo2, (405, 0), (430, 720), to_BGR(color), -1)

	### print keywords occurences
	occurrences = get_occurrences_from_words(words)
	for i in range(len(occurrences)):
		bottomLeftCornerOfText = (430, i * 40 + 20)
		cv2.putText(yo2, occurrences[i], bottomLeftCornerOfText, font, 1, white, 2)

	### print iteration number
	cv2.putText(yo2, "iteration: " + str(iteration), (700, 80), font, 2, white, 2)

	### print music name
	cv2.putText(yo2, "music: " + str(music_name), (700, 130), font, 2, white, 2)

	### print music name
	cv2.putText(yo2, "sound: " + str(sound_name), (700, 180), font, 2, white, 2)

	cv2.imshow("Control panel", yo2)

def get_occurrences_from_words(words):
	occurrences = [(word, words.count(word)) for word in set(words)]
	sorted_occurrences_str = [ word +' '+ str(occ) for word, occ in sorted(occurrences, key=lambda x:-x[1])]
	return sorted_occurrences_str

if __name__=="__main__":
    webcam = setup_webcam(FOCUS_VALUE)
    iteration = 1

    while(True):
        capture_frame(webcam, WINDOW_SIZE) # To remove the last frame from the buffer
        
        #### MAIN BODY OF THE LOOP
        

        try:
            frame = capture_frame(webcam, WINDOW_SIZE)
            text = extract_text(frame)
        	
            a1 = sanitize(text)

            music = get_music(a1)

            a2 = themes_to_count(a1)

            (r, g, b, brightness) = get_color(a2)
            sound = get_sound(a2)


            ### updating colors:
            if sound=="thunder_rain":
            	thunder(r, g, b)
            else:
            	display_new_color(r, g, b, brightness=brightness)

            play_sound(sound)
            play_music(music)
            display_frame(frame, a1, (r,g,b), iteration, music, sound)
        except Exception as e:
            print("someone screwed up here", e)
        #### END MAIN BODY

        key = cv2.waitKey(1)
        time.sleep(4)
        iteration+=1