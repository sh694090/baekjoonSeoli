from sys import stdin as s

for i in range(4):
    inp = list(map(int, s.readline().split()))
    for j in range(4):
        sum_val = sum(inp)
    print(sum_val)