import cv2
from google import genai
from PIL import Image
import re


def gemini_vision(image_data):
    """透過 Gemini 進行辨識"""
    client = genai.Client(api_key="YOUR API KEY")
    system_prompt = "辨識這張車牌的號碼‵，接下來我會傳送車牌的圖片，請只回傳車牌辨識內容"
    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=[system_prompt, image_data],
    )
    print(response.text)
    return response.text


def cv2_to_pil(cv2_image):
    """將 OpenCV 圖片轉換為 PIL 圖片。"""
    rgb_image = cv2.cvtColor(cv2_image, cv2.COLOR_BGR2RGB)
    pil_image = Image.fromarray(rgb_image)
    return pil_image


def get_license(img):
    """使用 Gemini API 辨識車牌。"""

    # 將 OpenCV 影像轉換為 Gemini API 接受的格式 Pillow Image
    pil_image = cv2_to_pil(img)

    response = gemini_vision(pil_image)
    # 提取辨識結果
    response_text = response.strip()
    # 使用正則表達式匹配車牌格式
    m = re.match(r'^[\w]{2,4}[-. ][\w]{2,4}$', response_text)
    if m:
        return m.group()
    else:
        return '找不到車牌'


try:
    img = cv2.imread('car.jpg')  # 讀取圖片
    print('status:  Start')
    text = get_license(img)  # 辨識圖片中的車牌
    print('車牌：', text)
    cv2.imshow('Frame', img)  # 顯示圖片
    cv2.waitKey(0)  # 等待
    cv2.destroyAllWindows()  # 關閉視窗
except Exception as e:
    print(f'讀取圖片失敗: {e}')
