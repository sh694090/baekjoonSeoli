from sys import stdin as s

inp = list(s.readline().strip())

result = []
for i in range(len(inp)):
    if inp[i].isalpha() == True:
        result.append(inp[i])

result = ''.join(result).upper()
print(result)



