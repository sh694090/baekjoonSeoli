from sys import stdin as s

inp = list(s.readline().strip())
num = int(s.readline().strip())

result = inp[::-1]

if len(result) < num:
    for elem in result:
        print(elem, end = "")
else:
    for i in range(num):
        print(result[i], end = "")