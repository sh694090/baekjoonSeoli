from sys import stdin as s

N = int(s.readline().rstrip())

for i in range(N):
    a, b = map(int, s.readline().split())

    sum = 0
    for j in range(a, b + 1):
        if j % 2 == 0:
            sum += j
    print(sum)