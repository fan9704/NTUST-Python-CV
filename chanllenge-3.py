import requests
from bs4 import BeautifulSoup
import re
from collections import Counter


class NewsScraper:
    def __init__(self, url="https://tw.yahoo.com"):
        self.url = url
        self.titles = []

    def fetch_news(self):
        print("📡 正在爬取 Yahoo 首頁新聞...")
        headers = {
            "User-Agent": "Mozilla/5.0"
        }
        response = requests.get(self.url, headers=headers)
        if response.status_code != 200:
            print("❌ 無法取得網頁內容。")
            return

        soup = BeautifulSoup(response.text, "html.parser")
        news_tags = soup.find_all("a")

        self.titles.clear()
        for tag in news_tags:
            text = tag.get_text(strip=True)
            if len(text) > 10:  # 粗略過濾：只收較長的標題
                self.titles.append(text)
                print(text)
        print(f"✅ 共取得 {len(self.titles)} 則可能的新聞標題。")

    def get_titles(self):
        return self.titles


class KeywordAnalyzer:
    def __init__(self):
        self.keyword_freq = Counter()

    def analyze(self, titles):
        print("🧠 正在進行關鍵字分析...")
        self.keyword_freq.clear()
        for title in titles:
            # 去除標點，轉小寫
            clean_title = re.sub(r"[^\w\u4e00-\u9fff]", " ", title)  # 保留中文字
            words = clean_title.split()
            for word in words:
                if len(word) > 1:  # 過濾單字詞（如 "的", "是"）
                    self.keyword_freq[word] += 1

    def show_top_keywords(self, top_n=5):
        print(f"\n📊 出現最多的 {top_n} 個關鍵詞：")
        for word, freq in self.keyword_freq.most_common(top_n):
            print(f"{word}：{freq} 次")


# 主選單互動
def show_menu():
    print("\n=== 即時新聞爬取與關鍵字分析 ===")
    print("1. 爬取最新新聞")
    print("2. 分析關鍵字")
    print("3. 離開系統")


# 主程式流程
scraper = NewsScraper()
analyzer = KeywordAnalyzer()

while True:
    show_menu()
    choice = input("請選擇操作（1-3）：")

    if choice == "1":
        scraper.fetch_news()
    elif choice == "2":
        titles = scraper.get_titles()
        if not titles:
            print("⚠️ 尚未爬取新聞，請先選擇選項 1。")
        else:
            analyzer.analyze(titles)
            analyzer.show_top_keywords()
    elif choice == "3":
        print("👋 系統結束，再見！")
        break
    else:
        print("⚠️ 無效選項，請重新輸入。")
