from sys import stdin as s

N = int(s.readline().strip())

arr = []
for _ in range(N):
    inp = int(s.readline().strip())
    arr.append(inp)

arr_sum = sum(arr)

result = str(arr_sum)
result = result[1:] + result[:1]
print(result)
