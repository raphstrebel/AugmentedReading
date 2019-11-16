import cv2
import pytesseract


# Define config parameters.
# '-l eng'  for using the English language
# '--oem 1' for using LSTM OCR Engine
config = ('-l eng --oem 1 --psm 3')

def sanitize_text(text):
  toReturn = text.split("\n")
  return toReturn


def extract_text(frame):
  extracted = pytesseract.image_to_string(frame, config=config)

  lines = extracted.split("\n")

  lines = list(filter(lambda a: len(a) > 0, lines))



  return lines