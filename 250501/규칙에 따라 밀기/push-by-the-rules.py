from sys import stdin as s

A = s.readline().strip()
command = list(s.readline().strip())

for i in range(len(command)):
    if command[i] == 'L':
        A = A[1:] + A[:1]
    else:
        A = A[-1:] + A[:-1]

print(A)