from sys import stdin as s

N = int(s.readline().rstrip())

cnt = 1
for i in range(2 * N - 1):
    for j in range(cnt):
        print("*", end = "")
    print()
    print()

    if i < N - 1:
        cnt += 1
    else:
        cnt -= 1