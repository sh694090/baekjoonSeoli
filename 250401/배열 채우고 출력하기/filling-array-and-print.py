from sys import stdin as s

inp = list(s.readline().split())
reversed_inp = inp[::-1]

for i in range(0, len(inp)):
    print(reversed_inp[i], end = "")