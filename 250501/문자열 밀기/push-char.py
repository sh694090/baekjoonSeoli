from sys import stdin as s

inp = s.readline().strip()

# 왼쪽으로 한 칸 이동 = 맨 왼쪽 문자가 맨 뒤로 이동
result = inp[1:] + inp[0]
print(result)