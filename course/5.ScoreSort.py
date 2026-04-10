# scores = list(map(int, input("請輸入學生分數，以空格分隔：").split()))
scores_str = input("請輸入學生分數，以空格分隔：").split(" ")

print("Raw Scores",scores_str)
scores = []
for score in scores_str:
    scores.append(int(score))
print("Scores:",scores)
highest_score = max(scores)
for score in scores:
    if score >= highest_score - 10:
        grade = "A"
    elif score >= highest_score - 20:
        grade = "B"
    elif score >= highest_score - 30:
        grade = "C"
    elif score >= highest_score - 40:
        grade = "D"
    else:
        grade = "F"
    print(f"分數: {score} -> 等級: {grade}")
