from sys import stdin as s

N = int(s.readline().rstrip())

arr = [[0] * N for _ in range(N)]

for i in range(N):
    for j in range(N):
        if i == 0 or j == 0:
            arr[i][j] = 1
        else:
            arr[i][j] = arr[i - 1][j] + arr[i - 1][j - 1] + arr[i][j - 1]

for row in arr:
    for elem in row:
        print(elem, end = " ")
    print()