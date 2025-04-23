from sys import stdin as s

N = int(s.readline().rstrip())

# 삼각형의 모양 배열로 만들어야겠지
arr = [[0] * (i + 1) for i in range(N)]

for i in range(N):
    for j in range(i + 1):
        if j == 0 or j == i:
            arr[i][j] = 1
        else:
            arr[i][j] = arr[i - 1][j - 1] + arr[i - 1][j]

for row in arr:
    for elem in row:
        print(elem, end = " ")
    print()