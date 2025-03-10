from sys import stdin as s

n = int(s.readline().rstrip())

is_com = False

for i in range(2, n - 1):
    if n % i == 0:
        is_com = True

if is_com == True:
    print('C')
else:
    print('N')