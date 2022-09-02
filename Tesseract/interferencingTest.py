import cv2
import pytesseract

noiseRemove = cv2.imread('research/noiseRemove.jpg')
text = pytesseract.image_to_data(noiseRemove, config = r'--oem 3 --psm 10 ', output_type=pytesseract.Output.DICT)
print(text['text'][4])