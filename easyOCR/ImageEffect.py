img_cropped = cv2.imread('cropped.png')
reader = easyocr.Reader(['en'], gpu=False)
result = reader.readtext(
    img_cropped, 
    allowlist = '0123456789')
print(result)