from sys import stdin as s

# 정수 10개를 입력받아
# 홀수 번째 입력받은 정수의 합, 짝수 번째 입력받은 정수의 합 중 큰 수 - 작은 수

arr = list(map(int, s.readline().split()))

even_arr = []
odd_arr = []
for i in range(len(arr)):
    if (i + 1) % 2 == 0:
        even_arr.append(arr[i])
    else:
        odd_arr.append(arr[i])

sum_even = sum(even_arr)
sum_odd = sum(odd_arr)

result = 0
if sum_even >= sum_odd:
    result = sum_even - sum_odd
else:
    result = sum_odd - sum_even

print(result)