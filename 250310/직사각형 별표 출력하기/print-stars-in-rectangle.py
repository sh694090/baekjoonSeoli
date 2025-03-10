# 별표 사이에 공백 두고 출력
from sys import stdin as s

N, M = map(int, s.readline().split())

for i in range(N):
    for j in range(M):
        print("*", end = " ")
    print()