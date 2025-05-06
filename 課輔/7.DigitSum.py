def sumDigits(n):
    if n < 10:
        return n
    else:
        return sumDigits(n // 10) + n % 10


number = int(input("請輸入正整數："))
print("各位數字總和為：", sumDigits(number))
