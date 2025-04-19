# 引入 OpenCV Python 函式庫
import cv2
# 建立顯示影像所需要的視窗 名稱為：FirstExample
cv2.namedWindow("FirstExample", cv2.WINDOW_AUTOSIZE)
# 等待按鍵接收
cv2.waitKey(0)
# 關閉視窗
cv2.destroyWindow("FirstExample")

