from sys import stdin as s

inp = list(s.readline().strip())

arr = []
for i in range(len(inp)):
    if inp[i].isalpha() == True or inp[i].isdigit() == True:
        arr.append(inp[i])
    

print(''.join(arr).lower())