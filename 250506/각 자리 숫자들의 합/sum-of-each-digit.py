from sys import stdin as s

n = list(s.readline().strip())

sum = 0
for elem in n:
    sum += int(elem)

print(sum)


