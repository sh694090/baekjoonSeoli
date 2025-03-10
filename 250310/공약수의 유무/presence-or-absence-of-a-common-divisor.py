from sys import stdin as s

A, B = map(int, s.readline().split())

is_common = False

# A 이상 B 이하의 수 중 1920과 2880의 공약수가 존재하는가?

for i in range(A, B + 1):
    if 1920 % i == 0 and 2880 % i == 0:
        is_common = True

if is_common == True:
    print(1)
else:
    print(0)