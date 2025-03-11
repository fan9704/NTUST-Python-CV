# 引入 OpenCV Python 函式庫
import cv2

# 建立顯示影像所需要的視窗 名稱為：FirstExample
cv2.namedWindow("FirstExample", cv2.WINDOW_AUTOSIZE)
# 從路徑 ./images/ntust.png 讀取圖片並以灰階儲存成 photo 變數
photo = cv2.imread("./images/ntust.png", cv2.IMREAD_GRAYSCALE)
# 顯示 photo 圖片變數 到 「FirstExample」視窗上
cv2.imshow("FirstExample", photo)
# 匯出圖片到 output 中 設置為 JPEG 且品質為 1 (區間 0~100)
cv2.imwrite("./output/ntust-grayscale-1.jpeg", photo,[cv2.IMWRITE_JPEG_QUALITY,1])
# 匯出圖片到 output 中 設置為 PNG 且品質為壓縮 9 (區間 0~9)
cv2.imwrite("./output/ntust-grayscale-9.png", photo,[cv2.IMWRITE_PNG_COMPRESSION,9])
# 等待按鍵接收
cv2.waitKey(0)
# 關閉視窗
cv2.destroyWindow("FirstExample")
