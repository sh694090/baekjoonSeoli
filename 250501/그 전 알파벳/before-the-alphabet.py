from sys import stdin as s

inp = s.readline().strip()

inp = ord(inp)

if inp == 97:
    result = chr(122)
else:
    result = chr(inp - 1)

print(result)