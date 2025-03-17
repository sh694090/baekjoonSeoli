from sys import stdin as s

N = int(s.readline().rstrip())

for i in range(1, N + 1):
    for j in range(i):
        print("* ", end = "")
    print()
    for j in range(N - i + 1):
        print("* ", end = "")
    print()