from sys import stdin as s

cnt = 0
while True:
    inp = int(s.readline().rstrip())

    if inp % 2 != 0:
        continue
    
    print(inp // 2)
    cnt += 1

    if cnt >= 3:
        break