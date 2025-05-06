def gcd(m, n):
    if m % n == 0:
        return n
    else:
        return gcd(n, m % n)

m = int(input("輸入第一個數字："))
n = int(input("輸入第二個數字："))
print("最大公因數為：", gcd(m, n))
