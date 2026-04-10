import cv2
import pytesseract

# 需要額外安裝 tesseract
# 如果不能執行請參考文章 https://blog.csdn.net/qq_44921056/article/details/117529269 他會引導你到這邊下載 https://tesseract-ocr.github.io/tessdoc/Installation.html
img = cv2.imread("./images/ntust.png")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
text = pytesseract.image_to_string(gray)

print("辨識出的文字：", text)
