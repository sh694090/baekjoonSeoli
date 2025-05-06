from sys import stdin as s

while True:
    inp = s.readline().strip()
    if inp == 'END':
        break
    else:
        print(inp[::-1])
    