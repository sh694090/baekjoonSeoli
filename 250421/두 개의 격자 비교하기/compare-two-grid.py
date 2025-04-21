from sys import stdin as s

# 2차원 배열 2개 입력
N, M = map(int, s.readline().split())

arr1 = [list(map(int, s.readline().split())) for _ in range(N)]
arr2 = [list(map(int, s.readline().split())) for _ in range(N)]

# 빈 2차원 배열 생성
result = [[0] * M for _ in range(N)]

for i in range(N):
    for j in range(M):
        if arr1[i][j] == arr2[i][j]:
            result[i][j] = 0
        else:
            result[i][j] = 1

for i in range(N):
    for j in range(M):
        print(result[i][j], end = " ")
    print()