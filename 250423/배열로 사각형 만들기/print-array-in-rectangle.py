from sys import stdin as s

# 크기 5 * 5의 2차원 배열
arr = [[0] * 5 for _ in range(5)]

# 첫번째 행, 첫번째 열 1로 초기화
for i in range(5):
    for j in range(5):
        arr[0][j] = 1
    arr[i][0] = 1

# 다른 칸은 바로 위의 값과 왼쪽 값 더함
for i in range(1, 5):
    for j in range(1, 5):
        arr[i][j] = arr[i - 1][j] + arr[i][j - 1]

for row in arr:
    for elem in row:
        print(elem, end = " ")
    print()