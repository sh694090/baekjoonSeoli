from sys import stdin as s
from collections import deque

N = int(s.readline().rstrip())

dq = deque()

for i in range(1, N + 1):
    dq.append(i)

for i in range (0, N - 1):
    dq.popleft()
    dq.append(dq.popleft())

print(dq[-1])