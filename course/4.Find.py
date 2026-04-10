def my_find(s1, s2):
    s1_length = len(s1)
    s2_length = len(s2)
    for start in range(s2_length - s1_length + 2):
        print(s2[start:start + s1_length])
        if s2[start:start + s1_length] == s1:
            return True
    return False


# abc 3
# dabcd 5
# abcxx 3 = 5-3+1
# xabcx
# xxabc
s1 = input("請輸入第一個字串：")
s2 = input("請輸入第二個字串：")

if my_find(s1, s2):
    print("是子字串")
else:
    print("不是子字串")
