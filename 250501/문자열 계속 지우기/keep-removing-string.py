from sys import stdin as s

A = s.readline().strip()
B = s.readline().strip()

while A.find(B) != -1:
    index = A.find(B)
    A = A[:index] + A[index + len(B):]
print(A)