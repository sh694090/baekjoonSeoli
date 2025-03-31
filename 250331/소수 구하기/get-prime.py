from sys import stdin as s

N = int(s.readline().rstrip())

for i in range(1, N + 1):
    if i == 1:
        continue
    isprime = True

    for j in range(2, i):
        if i % j == 0:
            isprime = False
    
    if isprime:
        print(i, end = " ")