from sys import stdin as s

A, B = map(int, s.readline().split())

sum = 0

# A 이상 B 이하
for i in range(A, B + 1):
    if i % 6 == 0:
        if i % 8 != 0:
            sum += i

print(sum)