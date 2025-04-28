from sys import stdin as s

inp = list(s.readline().strip())

result = []
for i in range(len(inp)):
    if (i + 1) % 2 == 0:
        result.append(inp[i])
    else:
        continue

for elem in result[::-1]:
    print(elem, end = "")