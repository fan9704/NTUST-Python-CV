# scores = list(map(int, input("請輸入學生分數，以空格分隔：").split()))

scores_str = input("請輸入學生分數，以空格分隔：").split(" ")
scores = []
for score in scores_str:
    scores.append(int(score))

for score in scores:
    if score >= 90:
        grade = "A"
    elif score >= 80:
        grade = "B"
    elif score >= 70:
        grade = "C"
    elif score >= 60:
        grade = "D"
    else:
        grade = "F"
    print(f"分數: {score} -> 等級: {grade}")
