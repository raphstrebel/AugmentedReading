import cv2 


def make_1080p(webcam):
    webcam.set(3, 1920)
    webcam.set(4, 1080)

def set_focus(webcam, focus_value):
    webcam.set(cv2.CAP_PROP_AUTOFOCUS, 0)
    webcam.set(cv2.CAP_PROP_FOCUS, focus_value)

def capture_frame(webcam, window_size):
    check, frame = webcam.read()
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    frame = cv2.adaptiveThreshold(frame, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, window_size, 25)
    return frame

def setup_webcam(focus_value):
    window_size = 55
    key = cv2. waitKey(1)
    webcam = cv2.VideoCapture(1)
    webcam.set(cv2.CAP_PROP_BUFFERSIZE, 1)
    make_1080p(webcam)
    set_focus(webcam, focus_value)
    return webcam
