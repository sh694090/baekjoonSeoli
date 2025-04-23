from sys import stdin as s

N = int(s.readline().rstrip())

arr = [[0] * N for _ in range(N)]

num = 1

for j in range(N - 1, -1, -1):
    if (N - 1 - j) % 2 == 0:
        for i in range(N - 1, -1, -1):
            arr[i][j] = num
            num += 1
    else:
        for i in range(N):
            arr[i][j] = num
            num += 1

for i in range(N):
    for j in range(N):
        print(arr[i][j], end = " ")
    print()
        