from sys import stdin as s

inp = list(s.readline().strip())

arr = []
for i in range(len(inp)):
    if ord(inp[i]) >= 65 and ord(inp[i]) <= 90:
        new = inp[i].lower()
        arr.append(new)
    else:
        new = inp[i].upper()
        arr.append(new)

print(''.join(arr))

