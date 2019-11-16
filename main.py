from video_capture import *
import cv2
import time

FOCUS_VALUE = 15
WINDOW_SIZE = 55

if __name__=="__main__":

    webcam = setup_webcam(FOCUS_VALUE)


    while(True):
        capture_frame(webcam, WINDOW_SIZE) # To remove the last frame from the buffer
        frame = capture_frame(webcam, WINDOW_SIZE)
        cv2.imshow("Capturing", frame)
        key = cv2.waitKey(1)
        time.sleep(2)


    
