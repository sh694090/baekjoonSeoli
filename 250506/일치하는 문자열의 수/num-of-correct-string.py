from sys import stdin as s

n, A = s.readline().split()

str_arr = []
for _ in range(int(n)):
    inp = s.readline().strip()
    str_arr.append(inp)

cnt = 0
for elem in str_arr:
    if elem == A:
        cnt += 1

print(cnt)