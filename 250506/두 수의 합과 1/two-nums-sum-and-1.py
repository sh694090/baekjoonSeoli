from sys import stdin as s

A, B = map(int, s.readline().split())

sum = A + B
sum = list(str(sum))

cnt = 0
for elem in sum:
    if elem == '1':
        cnt += 1

print(cnt)