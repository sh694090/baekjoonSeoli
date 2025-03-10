from sys import stdin as s

a, b, c = map(int, s.readline().split())

is_multiple = True

for i in range(a, b + 1):
    if i % c == 0:
        is_multiple = False

if is_multiple == True:
    print('YES')
else:
    print('NO')