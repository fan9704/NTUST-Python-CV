# 引入 OpenCV Python 函式庫
import cv2

# 建立顯示影像所需要的視窗 名稱為：FirstExample
cv2.namedWindow("FirstExample", cv2.WINDOW_AUTOSIZE)
# 從路徑 ./images/ntust.png 讀取圖片並以灰階儲存成 photo 變數
photo = cv2.imread("./images/ntust.png", cv2.IMREAD_GRAYSCALE)

# cv2.IMREAD_COLOR # RGB 讀取
# cv2.IMREAD_GRAYSCALE # 灰階讀取
# cv2.IMREAD_UNCHANGED # BGRA 讀取(包含 alpha 透明度資訊)

# 顯示 photo 圖片變數 到 「FirstExample」視窗上
cv2.imshow("FirstExample", photo)
# 等待按鍵接收
cv2.waitKey(0)
# 關閉視窗
cv2.destroyWindow("FirstExample")

