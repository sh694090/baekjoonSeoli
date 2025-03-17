from sys import stdin as s

N = int(s.readline().rstrip())

for i in range(N):
    for _ in range(N - i):
        print("* ", end = "")
    print()
    for _ in range(i + 1):
        print("* ", end = "")
    print()