from sys import stdin as s

N = int(s.readline().rstrip())

arr = [[0] * N for _ in range(N)]

num = 1
for i in range(N):
    for j in range(N):
        arr[j][i] = num
        num += 1

for i in range(N):
    for j in range(N):
        print(arr[i][j], end = " ")
    print()