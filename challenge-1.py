# 超市進銷存系統（基礎版）

# 商品資料庫：每個商品是 dict，儲存在 product_list 裡面
product_list = []

# 總營收
total_revenue = 0


# 主選單
def show_menu():
    print("\n=== 超市進銷存系統 ===")
    print("1. 新增商品")
    print("2. 銷售商品")
    print("3. 查詢庫存")
    print("4. 統計總營收")
    print("5. 離開系統")


# 新增商品
def add_product():
    name = input("輸入商品名稱：")
    price = float(input("輸入商品單價："))
    stock = int(input("輸入庫存數量："))
    product = {
        "name": name,
        "price": price,
        "stock": stock
    }
    product_list.append(product)
    print(f"✅ 商品「{name}」已新增成功。")


# 查找商品（依名稱）
def find_product(name):
    for product in product_list:
        if product["name"] == name:
            return product
    return None


# 銷售商品
def sell_product():
    global total_revenue
    name = input("輸入要購買的商品名稱：")
    product = find_product(name)
    if not product:
        print("❌ 查無此商品！")
        return
    quantity = int(input("輸入購買數量："))
    if quantity <= product["stock"]:
        total = quantity * product["price"]
        product["stock"] -= quantity
        total_revenue += total
        print(f"✅ 購買成功，總金額：{total:.2f} 元")
    else:
        print("❌ 庫存不足，無法完成交易。")


# 查詢庫存
def show_inventory():
    if not product_list:
        print("⚠️ 目前沒有商品資料。")
        return
    print("\n=== 商品庫存清單 ===")
    for product in product_list:
        print(f"名稱：{product['name']} | 單價：{product['price']:.2f} | 庫存：{product['stock']}")


# 顯示總營收
def show_revenue():
    print(f"\n📊 目前總營收為：{total_revenue:.2f} 元")


# 主程式迴圈
while True:
    show_menu()
    choice = input("請選擇操作（1-5）：")

    if choice == "1":
        add_product()
    elif choice == "2":
        sell_product()
    elif choice == "3":
        show_inventory()
    elif choice == "4":
        show_revenue()
    elif choice == "5":
        print("👋 感謝使用，再見！")
        break
    else:
        print("⚠️ 無效的選項，請重新輸入。")
