from sys import stdin as s

inp = list(s.readline().rstrip())
alp = s.readline().rstrip()

cnt = 0
for elem in inp:
    if elem == alp:
        cnt += 1

print(cnt)