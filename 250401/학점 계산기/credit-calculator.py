from sys import stdin as s

N = int(s.readline().rstrip())
grade_arr = list(map(float, s.readline().split()))

grade_sum = sum(grade_arr)
grade_avg = grade_sum / N

# 4.0 이상: Perfect
# 3.0 이상: Good
# 3.0 미만: Poor


if grade_avg >= 4:
    result = "Perfect"
elif grade_avg >= 3:
    result = "Good"
else:
    result = "Poor"

print(f"{grade_avg:.1f}")
print(result)