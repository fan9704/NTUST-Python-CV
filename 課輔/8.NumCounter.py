# nums = list(map(int, input("請輸入一連串正整數：").split()))
raw_nums = input("請輸入一連串正整數：").split()
nums = []
for num in raw_nums:
    nums.append(int(num))

counter = {}

for num in nums:
    counter[num] = counter.get(num, 0) + 1

max_freq = max(counter.values())
most_common = []

for k,v in counter.items():
    if v == max_freq:
        most_common.append(k)

print("出現最多次的數字：", most_common)
print("出現次數：", max_freq)
