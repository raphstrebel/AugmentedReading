import cv2
import pytesseract


# Define config parameters.
# '-l eng'  for using the English language
# '--oem 1' for using LSTM OCR Engine
config = ('-l eng --oem 1 --psm 4')

def extract_text(frame):
  extracted = pytesseract.image_to_string(frame, config=config)
  extracted = extracted.replace("\n", " ")
  return extracted