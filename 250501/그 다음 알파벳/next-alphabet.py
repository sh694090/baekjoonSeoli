from sys import stdin as s

inp = s.readline().strip()

inp = ord(inp)

if inp == 122:
    result = chr(97)
else:
    result = chr(inp + 1)

print(result)