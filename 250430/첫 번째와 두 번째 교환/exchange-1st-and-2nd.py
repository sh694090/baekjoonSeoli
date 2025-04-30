from sys import stdin as s

inp = s.readline().strip()
inp_arr = list(inp)

first = inp[0]
second = inp[1]

for i in range(len(inp)):
    if inp_arr[i] == first:
        inp_arr[i] = second
    elif inp_arr[i] == second:
        inp_arr[i] = first

result = ''.join(inp_arr)
print(result)