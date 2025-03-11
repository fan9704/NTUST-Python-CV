import cv2

try:
    img = cv2.imread("./images/ntust.png")
    # 改變尺寸為 (300,100)
    img_resized = cv2.resize(img,(300,100))
    cv2.imshow("Origin Photo",img)
    cv2.imshow("Resized Photo",img_resized)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    try:
        cv2.imwrite("./output/resized-ntust.png",img_resized)
        print("Saved resized image")
    except:
        print("Error:write")
except:
    print("Error:read")