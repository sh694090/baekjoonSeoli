from sys import stdin as s

# 입력받는 정수의 개수
N = int(s.readline().rstrip())

sum = 0
avg = 0

# N개의 정수 입력받기
for i in range(N):
    num = int(s.readline().rstrip())
    sum += num
    avg = sum / (i + 1)

print(sum, f"{avg:.1f}")