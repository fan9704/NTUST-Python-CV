# 國立台灣科技大學-資訊管理系 Python 程式設計

---

## 有關 Python venv 虛擬環境

### 建立虛擬環境

```shell
# Windows
python -m venv [虛擬環境名稱]
# MacOS/Linux
python3 -m venv [虛擬環境名稱]
```

### 進入虛擬環境

```shell
# Windows
./[虛擬環境名稱]/Scripts/activate.ps1
# MacOS/Linux
./[虛擬環境名稱]/Scripts/activate
```

### 根據 requirements.txt 安裝套件

```shell
pip install -r requirements.txt
```

### 離開虛擬環境(不需要使用時執行)

```shell
deactive
```

---

## 不使用虛擬環境，直接裝 OpenCV 也可以

### 安裝 OpenCV 套件

```shell
pip install opencv-python
```

---

## 教學內容

1. 讀取照片 
2. 讀取照片成灰階
3. 寫入照片成灰階
4. 寫入低像素照片
5. 修改照片比例
6. 基本攝像頭認識
7. 車牌辨識
8. 專案 - 顏色追蹤
9. 專案 - 攝像頭濾鏡
10. 專案 - 辨識圖片文字
11. 專案 - 臉部追蹤

---

## 參考資料

1. [Medium - Python 虛擬環境--venv](https://dev.to/codemee/python-xu-ni-huan-jing-venv-nbg)