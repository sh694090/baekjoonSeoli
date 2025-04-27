from sys import stdin as s

# 문자열 10개 공백을 사이에 두고 주어짐
inp = tuple(s.readline().split())

sum = 0
for elem in inp:
    sum += len(elem)

print(sum)