from sys import stdin as s

A = s.readline().strip()
B = s.readline().strip()

cnt = 0
for _ in range(len(A)):
    if A == B:
        print(cnt)
        break
    else:
        cnt += 1
        A = A[-1:] + A[:-1]

if cnt == len(A):
    print(-1)