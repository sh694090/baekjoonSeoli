from sys import stdin as s

N = int(s.readline().rstrip())

for i in range(1, N + 1):
    if i % 2 == 0:
        for j in range(i):
            print("*", end = " ")
        print()
    else:
        print("*")