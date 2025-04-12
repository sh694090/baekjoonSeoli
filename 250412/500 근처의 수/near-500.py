from sys import stdin as s

# 10개 정수 입력받아
# 500 미만의 가장 큰 수와 500 초과의 수 중 가장 작은 수 출력

arr = list(map(int, s.readline().split()))

# 500 미만인 애들만
arr_less = []
for elem in arr:
    if elem < 500:
        arr_less.append(elem)

max_val = max(arr_less)

# 500 초과인 애들만
arr_more = []
for elem in arr:
    if elem > 500:
        arr_more.append(elem)

min_val = min(arr_more)

print(max_val, min_val)