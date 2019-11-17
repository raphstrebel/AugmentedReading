from video_capture import *
from text_extraction import *
from lamp_handler import *
from themes_dict import *
from text_to_colors import *
from prepare_analysis import *
from play_music import *
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

def display_frame(frame, text, color, iteration, music_name, sound_name):
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
	occurrences = get_occurrences_from_text(text)
	for i in range(len(occurrences)):
		bottomLeftCornerOfText = (430, i * 40 + 20)
		cv2.putText(yo2, occurrences[i], bottomLeftCornerOfText, font, 1, white, 2)

	### print iteration number
	cv2.putText(yo2, "iteration: " + str(iteration), (700, 80), font, 2, white, 2)

	### print music name
	cv2.putText(yo2, "music: " + music_name, (700, 130), font, 2, white, 2)

	### print music name
	cv2.putText(yo2, "sound: " + sound_name, (700, 180), font, 2, white, 2)

	cv2.imshow("Control panel", yo2)

def get_occurrences_from_text(text):
	keywords = get_keywords_from_text(text)
	occurrences = [(word, keywords.count(word)) for word in set(keywords)]
	sorted_occurrences_str = [ word +' '+ str(occ) for word, occ in sorted(occurrences, key=lambda x:-x[1])]
	return sorted_occurrences_str

if __name__=="__main__":
    webcam = setup_webcam(FOCUS_VALUE)
    iteration = 1

    while(True):
        capture_frame(webcam, WINDOW_SIZE) # To remove the last frame from the buffer
        
        #### MAIN BODY OF THE LOOP
        frame = capture_frame(webcam, WINDOW_SIZE)
        text = extract_text(frame)

        args = get_all_parameters(text)
        music = get_music(args)
        sound = get_sound(args)
        (r, g, b, brightness) = get_color(args)#

        display_new_color(r, g, b, brightness=brightness)
        display_frame(frame, text, (r,g,b), iteration, music, sound)
        #### END MAIN BODY

        key = cv2.waitKey(1)
        time.sleep(2)
        iteration+=1