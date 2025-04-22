from sys import stdin as s

N, M = map(int, s.readline().split())

arr = [[0] * M for _ in range(N)]

num = 0
# i가 짝수인 경우 j가 1씩 증가
# i가 홀수인 경우 j가 1씩 감소
for i in range(M):
    if i % 2 == 0:
        for j in range(N):
            arr[j][i] = num
            num += 1
    else:
        for j in range(N - 1, -1, -1):
            arr[j][i] = num
            num += 1

for i in range(N):
    for j in range(M):
        print(arr[i][j], end = " ")
    print()