from sys import stdin as s

inp = list(s.readline().strip())
num = int(s.readline().strip())

result = inp[::-1]

for i in range(num):
    print(result[i], end = "")