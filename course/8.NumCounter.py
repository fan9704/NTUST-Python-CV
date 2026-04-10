# nums = list(map(int, input("請輸入一連串正整數：").split()))
raw_nums = input("請輸入一連串正整數：").split(" ")
print("Raw Nums",raw_nums)
nums = []
for num in raw_nums:
    nums.append(int(num))
print("Nums",nums)
counter = dict()

for num in nums:
    counter[num] = counter.get(num, 0) + 1
print("Counter",counter)
max_freq = max(counter.values())
most_common = []

for k,v in counter.items():
    if v == max_freq:
        most_common.append(k)

print("出現最多次的數字：", most_common)
print("出現次數：", max_freq)
