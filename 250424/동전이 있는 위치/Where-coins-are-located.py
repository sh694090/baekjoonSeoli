from sys import stdin as s

# N: 격자의 크기
# M: 동전의 개수
N, M = map(int, s.readline().split())

# 두번째 줄부터 M개의 줄에 걸쳐 (r, c) 값이 공백 사이에 두고 주어짐
# (r, c) => 해당 점이 r행 c열에 놓여야 함

# 빈 배열 생성
arr = [[0] * N for _ in range(N)]

for _ in range(M):
    r, c = map(int, s.readline().split())
    arr[r - 1][c - 1] = 1

for row in arr:
    for elem in row:
        print(elem, end = " ")
    print()
    
    


