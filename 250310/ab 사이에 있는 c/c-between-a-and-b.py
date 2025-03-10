from sys import stdin as s

a, b, c = map(int, s.readline().split())

is_even = False

for i in range(a, b + 1):
    if i % c == 0:
        is_even = True

if is_even == True:
    print('YES')
else:
    print('NO')