from sys import stdin as s

inp = list(s.readline().split())

word = inp[0]
Q = int(inp[1])

# 요청이 Q개 주어짐
for _ in range(Q):
    req = int(s.readline().strip())
    if req == 1:
        word = word[1:] + word[:1]
    elif req == 2:
        word = word[-1:] + word[:-1]
    elif req == 3:
        word = word[::-1]
    print(word)