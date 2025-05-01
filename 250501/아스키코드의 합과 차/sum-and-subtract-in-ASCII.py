from sys import stdin as s

A, B = s.readline().split()

A = ord(A)
B = ord(B)

if A >= B:
    print(A + B, A - B)
else:
    print(A + B, B - A)