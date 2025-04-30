from sys import stdin as s

A = s.readline().strip()
B = s.readline().strip()

cnt = 0
if B in A:
    for i in range(len(A) - 1):
        if A[i] == B[0] and A[i + 1] == B[1]:
            cnt += 1

print(cnt)