from sys import stdin as s

A, B = map(int, s.readline().split())

prod = 1

for i in range(A, B + 1):
    prod *= i

print(prod)