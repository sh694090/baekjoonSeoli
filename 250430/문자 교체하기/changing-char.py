from sys import stdin as s

inp = s.readline().split()

str1_arr = list(inp[0])
str2_arr = list(inp[1])

result = str1_arr[:2] + str2_arr[2:]

print(''.join(result))
