from sys import stdin as s 

A = list(s.readline().strip())

arr = []
for i in range(len(A)):
    if A[i].isdigit() == True:
        arr.append(A[i])

arr = list(map(int, arr))
result = sum(arr)
print(result)