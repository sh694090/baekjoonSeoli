from sys import stdin as s

N = int(s.readline().rstrip())

# 공백 먼저 출력하고 별 출력

for i in range(N):
    for j in range(1, N - i):
        print(" ", end = "")
    for j in range(i + 1):
        print("*", end = " ")
    print()

for i in range(1, N):
    for j in range(i):
        print(" ", end = "")
    for j in range(N - i):
        print("*", end = " ")
    print()