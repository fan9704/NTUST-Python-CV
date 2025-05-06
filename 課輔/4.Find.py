def my_find(sub, main):
    for i in range(len(main) - len(sub) + 1):
        if main[i:i + len(sub)] == sub:
            return True
    return False


s1 = input("請輸入第一個字串：")
s2 = input("請輸入第二個字串：")

if my_find(s1, s2):
    print("是子字串")
else:
    print("不是子字串")
