import random

computer = random.randint(0, 2)
user = int(input("請輸入 0 (剪刀)、1 (石頭)、2 (布)："))

print(f"你出的是 {user}，電腦出的是 {computer}")

# 0剪刀, 1石頭, 2布
if user == computer:
    print("平手")
elif (user == 0 and computer == 2) or (user == 1 and computer == 0) or (user == 2 and computer == 1):
    print("你贏了！")
else:
    print("你輸了！")
