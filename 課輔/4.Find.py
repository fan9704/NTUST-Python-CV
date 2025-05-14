def my_find(s1,s2):
    s1_length = len(s1)
    s2_length = len(s2)
    for start in range(s2_length-s1_length +1):
        if s2[start:start+3] == s1:
            return True
    return False


s1 = input("請輸入第一個字串：")
s2 = input("請輸入第二個字串：")

if my_find(s1, s2):
    print("是子字串")
else:
    print("不是子字串")
