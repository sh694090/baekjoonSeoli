from sys import stdin as s

A, B = s.readline().split()

arr_A = list(A)
print(arr_A)
num_A = []
for i in range(len(arr_A)):
    if arr_A[i].isdigit() != True:
        break
    else:
        num_A.append(arr_A)

print(num_A)

# arr_B = list(B)
# num_B = []
# for i in range(len(arr_B)):
#     if arr_B[i].isdigit() != True:
#         break
#     else:
#         num_B.append(arr_B)

# result = int(''.join(arr_A)) + int(''.join(arr_B))
# print(result)