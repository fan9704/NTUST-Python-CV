import cv2

# 建立攝影機物件 裡面的數字是指攝影機編號(預設 0)
camera = cv2.VideoCapture(0)
# 確認攝影機是否已經打開
print(f"Camera is Open:{camera.isOpened()}")
# 讀取攝影機影像
# success, img = camera.read()
# cv2.imshow("FirstVideo",img)
# cv2.imwrite("./output/first-video.png",img)

# 持續輸出影像
while True:
    success, img = camera.read()  # 不斷從攝影機讀取畫面
    if success:
        cv2.imshow("SecondVideo", img)
    # 接收使用者按下按鍵等待 10ms
    key = cv2.waitKey(10)
    print(key)
    # 當按下 q 跳脫迴圈
    if key == ord("q"):
        cv2.destroyAllWindows()
        print("End Capture")
        break
    # 當按下 s 儲存畫面
    if key == ord("s"):
        cv2.imwrite("./output/snapshot.png",img)
        print("ScreenShot")


# 程式結束釋放攝影機資源
camera.release()
print("Release Camera")