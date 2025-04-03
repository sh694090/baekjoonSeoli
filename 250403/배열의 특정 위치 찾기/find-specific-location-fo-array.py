from sys import stdin as s

arr = list(map(int, s.readline().split()))

# 인덱스가 짝수인 값의 합
# 앤나 인덱스가 3의 배수인 값의 합
# 이렇게 2개를 출력

# 인덱스가 짝수인 애들만 따로 배열로 출력해야하나
# 각 인덱스에 맞는 애들만 배열로 출력해야하나

even_arr = []
for i in range(len(arr)):
    if (i + 1) % 2 == 0:
        even_arr.append(arr[i])
    else:
        continue
sum_even_arr = sum(even_arr)

multiple_arr = []
for i in range(len(arr)):
    if (i + 1) % 3 == 0:
        multiple_arr.append(arr[i])
    else:
        continue
sum_multiple_arr = sum(multiple_arr)
avg_multiple_arr = sum_multiple_arr / len(multiple_arr)

print(sum_even_arr, f"{avg_multiple_arr:.1f}")