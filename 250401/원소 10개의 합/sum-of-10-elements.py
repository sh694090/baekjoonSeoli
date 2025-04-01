from sys import stdin as s

# 주어진 입력을 int로 바꿔서 배열로 입력 받음
inp = list(map(int, s.readline().split()))

sum = 0
for i in range(0, len(inp)):
    sum += inp[i]
print(sum)