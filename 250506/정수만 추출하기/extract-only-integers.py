from sys import stdin as s

A, B = s.readline().split()

arr_A = list(A)
num_A = []
for i in range(len(arr_A)):
    if arr_A[i].isdigit() != True:
        break
    else:
        num_A.append(arr_A[i])

A = ''.join(num_A)

arr_B = list(B)
num_B = []
for i in range(len(arr_B)):
    if arr_B[i].isdigit() != True:
        break
    else:
        num_B.append(arr_B[i])

B = ''.join(num_B)

result = int(A) + int(B)
print(result)