from sys import stdin as s

N = int(s.readline().rstrip())

for x in range(11):
    if N == 2 ** x:
        print(x)
        break