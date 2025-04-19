from sys import stdin as s

# 4열 4행 배열 입력받음
arr = [list(map(int, s.readline().split())) for _ in range(4)]

# 색칠된 칸에 해당하는 정수의 합
sum = 0
for i in range(1, 5):
    for j in range(1, i + 1):
        sum += arr[i - 1][j - 1]

print(sum)