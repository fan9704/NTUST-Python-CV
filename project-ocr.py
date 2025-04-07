import cv2
import pytesseract

# 需要額外安裝 tesseract
img = cv2.imread("./images/ntust.png")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
text = pytesseract.image_to_string(gray)

print("辨識出的文字：", text)
