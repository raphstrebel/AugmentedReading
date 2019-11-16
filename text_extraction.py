import cv2
import pytesseract


# Define config parameters.
# '-l eng'  for using the English language
# '--oem 1' for using LSTM OCR Engine
config = ('-l eng --oem 1 --psm 3')

def extract_text(frame):
  return pytesseract.image_to_string(frame, config=config)