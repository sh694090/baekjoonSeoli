from sys import stdin as s

N = int(s.readline().rstrip())

i = 1
cnt = 0
prod = int(N)

while prod >= 0:
    if prod // i <= 1:
        break
    prod /= i
    i += 1
    cnt += 1
print(cnt + 1)