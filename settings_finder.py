import cv2
import numpy as np
from sys import platform

current_focus = 0
window_size = 55

def is_mac_os():
    return platform == "darwin"

def make_1080p(webcam):
    webcam.set(3, 1920)
    webcam.set(4, 1080)

def set_focus(webcam):
    if(is_mac_os):
        print("settting focus not allowed on macos")
        return

    webcam.set(cv2.CAP_PROP_AUTOFOCUS, 0) # disable autofocus
    print("setting focus to: ", current_focus)
    webcam.set(cv2.CAP_PROP_FOCUS, current_focus)

def process_frame(frame):
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    frame = cv2.adaptiveThreshold(frame, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, window_size, 25)
    frame = cv2.resize(frame, (960, 540))
    frame = np.rot90(frame)
    return frame

if __name__ == "__main__":
    
    webcam = cv2.VideoCapture(1)
    make_1080p(webcam)
    set_focus(webcam)

    while True:
        try:
            check, frame = webcam.read()
            frame = process_frame(frame)
            cv2.imshow("input", frame)

            key = cv2.waitKey(1)
            if key == ord('y'):
                current_focus -= 5
                set_focus(webcam)
            
            elif key == ord('x'):
                current_focus += 5
                set_focus(webcam)
                
            
        except(KeyboardInterrupt):
            webcam.release()
            cv2.destroyAllWindows()
            break