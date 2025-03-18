from sys import stdin as s

N = int(s.readline().rstrip())

for i in range(2 * N + 1):
    if i % 2 == 0:
        for _ in range(2 * N + 1):
            print("*", end = " ")
        print()
    else:
        for j in range(2 * N + 1):
            if j % 2 == 0:
                print("*", end = " ")
            else:
                print(" ", end = " ")
        print()