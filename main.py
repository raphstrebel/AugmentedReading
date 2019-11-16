from video_capture import *
from text_extraction import *
from lamp_handler import *
from color_getter import *
from themes_dict import *
from text_to_colors import *
import cv2
import time

FOCUS_VALUE = 15
WINDOW_SIZE = 55

def display_frame(frame, text, color):

	### hack
	cv2.imwrite('todel.png', frame)

	### second hack
	yo = cv2.imread('todel.png', cv2.IMREAD_COLOR)
	yo = cv2.resize(yo, (405, 720))
	cv2.imwrite("todel2.png", yo)
	yo2 = cv2.imread("todel2.png")

	### Oufff, we're good to go :-)
	yo2 = cv2.copyMakeBorder(yo2, 0, 0, 0, 800, cv2.BORDER_CONSTANT)

	cv2.rectangle(yo, (405, 0), (430, 720), [int(i*255) for i in color], -1)


	font                   = cv2.FONT_HERSHEY_SIMPLEX 	
	fontScale              = 1
	fontColor              = (255, 255, 255)
	lineType               = 2

	for i in range(len(text)):
		bottomLeftCornerOfText = (430, i * 40 + 20)
		cv2.putText(yo2, text[i], bottomLeftCornerOfText, font, fontScale,fontColor,lineType)

	cv2.imshow("Capturing", yo2)

if __name__=="__main__":

    webcam = setup_webcam(FOCUS_VALUE)


    while(True):
        capture_frame(webcam, WINDOW_SIZE) # To remove the last frame from the buffer
        
        #### MAIN BODY OF THE LOOP
        frame = capture_frame(webcam, WINDOW_SIZE)
        text = extract_text(frame)
        #color = get_color_for_words(text)
        #text = "him—“we are now close upon the Norwegian coast—in the sixty-eighth degree of latitude— in the great province of Nordland—and in the dreary district of Lofoden.  e mountain upon whose top we sit is Helseggen, the Cloudy. Now raise yourself up a little higher—hold on to the grass if you feel giddy—so—and look out, beyond the belt of vapor beneath us, into the sea.” I looked dizzily, and beheld a wide expanse of ocean, whose waters wore so inky a hue as to bring at once to my mind the Nubian geographer’s account of the Mare Tenebrarum. A panorama more deplorably desolate no hu- man imagination can conceive. To the right and left, as far as the eye could reach, there lay outstretched, like ramparts of the world, lines of horridly black and beetling cli , whose character of gloom was but the more forcibly illustrated by the surf which reared high up against its white and ghastly crest, howling and shrieking forever. Just opposite the promon- tory upon whose apex we were placed, and at a distance of some  ve or six miles out at sea, there was visible a small, bleak-looking island; or, more properly, its position was discern- ible through the wilderness of surge in which it was enveloped. About two miles nearer the land, arose another of smaller size, hideously craggy and barren, and encompassed at vari- ous intervals by a cluster of dark rocks.  e appearance of the ocean, in the space between the more distant island and the shore, had something very unusual about it. Although, at the time, so strong a gale was blowing land- ward that a brig in the remote o ng lay to"
        r,g,b, brightness = text_to_colors_and_emotions(text)
        print(r,g,b,brightness)
        displayNewColor(r,g,b,brightness=brightness)
        display_frame(frame, text, color=(r,b,g))

        #### END MAIN BODY

        key = cv2.waitKey(1)
        time.sleep(2)


    
