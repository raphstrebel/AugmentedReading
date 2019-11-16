import cv2

key = cv2. waitKey(1)
webcam = cv2.VideoCapture(1)

focus = 0

def make_1080p(webcam):
    webcam.set(3, 1920)
    webcam.set(4, 1080)

def set_focus(webcam, focus_value):
    #webcam.set(cv2.CAP_PROP_AUTOFOCUS, 0)
    print("setting focus to: ", focus_value)
    #webcam.set(cv2.CAP_PROP_FOCUS, focus_value)

#def capture_frame(webcam, window_size):
#    check, frame = webcam.read()
#    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#    frame = cv2.adaptiveThreshold(frame, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, window_size, 25)

make_1080p(webcam)
set_focus(webcam, focus)

while True:
    try:
        check, frame = webcam.read()
        #print(check) #prints true as long as the webcam is running
        #print(frame) #prints matrix values of each framecd 

        frame = cv2.resize(frame, (960, 540))   
        cv2.imshow("Capturing", frame)
        key = cv2.waitKey(1)
        if key == ord('s'): 
            cv2.imwrite(filename='saved_img.jpg', img=frame)
            webcam.release()
            img_new = cv2.imread('saved_img.jpg', cv2.IMREAD_GRAYSCALE)
            img_new = cv2.imshow("Captured Image", img_new)
            cv2.waitKey(1650)
            cv2.destroyAllWindows()
            print("Processing image...")
            img_ = cv2.imread('saved_img.jpg', cv2.IMREAD_ANYCOLOR)
            print("Converting RGB image to grayscale...")
            gray = cv2.cvtColor(img_, cv2.COLOR_BGR2GRAY)
            print("Converted RGB image to grayscale...")
            print("Resizing image to 28x28 scale...")
            img_ = cv2.resize(gray,(28,28))
            print("Resized...")
            img_resized = cv2.imwrite(filename='saved_img-final.jpg', img=img_)
            print("Image saved!")
        
            break
        elif key == ord('q'):
            print("Turning off camera.")
            webcam.release()
            print("Camera off.")
            print("Program ended.")
            cv2.destroyAllWindows()
            break
        elif key == ord('y'):
            focus -= 5
            set_focus(webcam, focus)
            
        elif key == ord('x'):
            set_focus(webcam, focus)
            focus += 5
            

        
    except(KeyboardInterrupt):
        print("Turning off camera.")
        webcam.release()
        print("Camera off.")
        print("Program ended.")
        cv2.destroyAllWindows()
        break