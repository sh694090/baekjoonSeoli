from sys import stdin as s

grade_arr = list(map(float, s.readline().split()))
grade_sum = sum(grade_arr)
grade_avg = grade_sum / 8

print(f"{grade_avg:.1f}")