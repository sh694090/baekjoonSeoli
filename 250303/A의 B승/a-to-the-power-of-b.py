from sys import stdin as s

A, B = map(int, s.readline().split())

prod = 1

for i in range(B):
    prod *= A

print(prod)