from sys import stdin as s

N, M = map(int, s.readline().split())

arr = [[0] * N for _ in range(N)]

num = 1
for _ in range(M):
    r, c = map(int, s.readline().split())
    arr[r - 1][c - 1] = num
    num += 1

for row in arr:
    for elem in row:
        print(elem, end = " ")
    print()