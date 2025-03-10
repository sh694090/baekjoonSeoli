from sys import stdin as s

N = int(s.readline().rstrip())

for i in range(N):
    for j in range(i + 1):
        print("*", end = " ")
    print()