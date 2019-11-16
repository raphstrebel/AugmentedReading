from video_capture import *
from text_extraction import *
from lamp_handler import *
from color_getter import *
import cv2
import time

FOCUS_VALUE = 15
WINDOW_SIZE = 55

def display_frame(frame, text):

	### hack
	cv2.imwrite('todel.png', frame)

	### second hack
	yo = cv2.imread('todel.png', cv2.IMREAD_COLOR)
	yo = cv2.resize(yo, (405, 720))
	cv2.imwrite("todel2.png", yo)
	yo2 = cv2.imread("todel2.png")

	### Oufff, we're good to go :-)
	yo2 = cv2.copyMakeBorder(yo2, 0, 0, 0, 800, cv2.BORDER_CONSTANT)


	font                   = cv2.FONT_HERSHEY_SIMPLEX 	
	fontScale              = 1
	fontColor              = (255, 255, 255)
	lineType               = 2

	for i in range(len(text)):
		bottomLeftCornerOfText = (405, i * 40 + 20)
		cv2.putText(yo2, text[i], bottomLeftCornerOfText, font, fontScale,fontColor,lineType)

	cv2.imshow("Capturing", yo2)

if __name__=="__main__":

    webcam = setup_webcam(FOCUS_VALUE)


    while(True):
        capture_frame(webcam, WINDOW_SIZE) # To remove the last frame from the buffer
        
        #### MAIN BODY OF THE LOOP
        frame = capture_frame(webcam, WINDOW_SIZE)
        text = extract_text(frame)
        color = get_color_for_words(text)
        displayNewColor(*color)
        display_frame(frame, text)

        #### END MAIN BODY

        key = cv2.waitKey(1)
        time.sleep(2)


    
