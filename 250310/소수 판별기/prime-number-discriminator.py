from sys import stdin as s

N = int(s.readline().rstrip())

is_primenum = True

for i in range(2, N):
    if N % i == 0:
        is_primenum = False

if is_primenum == True:
    print('P')
else:
    print('C')