import pytesseract
import cv2
import matplotlib.pyplot as plt

path_image  = r'G:\Program\Python\OCR_Detection\itron_meteran.jpg'
img         = cv2.imread(path_image)
img_cropped = img[180:225,  205:382]

cv2.imwrite('G:\Program\Python\OCR_Detection\itron_meteran_cropped.jpg', img_cropped)

fig = plt.figure()
fig.add_subplot(221)
plt.imshow('G:\Program\Python\OCR_Detection\itron_meteran.jpg')
fig.add_subplot(221)
plt.imshow('G:\Program\Python\OCR_Detection\itron_meteran_cropped.jpg')

plt.show()
cv2.waitKey(0)
