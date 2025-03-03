from sys import stdin as s

N = int(s.readline().rstrip())

cnt = 0

for i in range(1, N + 1):
    if i % 2 == 0:
        continue
    elif i % 3 == 0:
        continue
    elif i % 5 == 0:
        continue
    else:
        cnt += 1

print(cnt)