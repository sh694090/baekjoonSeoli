from sys import stdin as s

# 2행 4열의 배열
# 가로 평균
# 세로 평균
# 전체 평균
# 이걸 소수 첫째자리까지 출력

# 배열 전체 입력받기
arr_2d = []
for i in range(2):
    arr_1d = list(map(int, s.readline().split()))
    arr_2d.append(arr_1d)

# 가로 평균
for i in range(2):
    for j in range(4):
        sum_val = sum(arr_2d[i])
    row_avg = sum_val / 4
    print(f"{row_avg:.1f}", end = " ")
print()

# 세로 평균
for j in range(4):
    sum_val = 0
    for i in range(2):
        sum_val += arr_2d[i][j]
    col_avg = sum_val / 2
    print(f"{col_avg:.1f}", end = " ")
print()
        

# 전체 평균
sum_val = sum(sum(row) for row in arr_2d)
all_avg = sum_val / 8
print(f"{all_avg:.1f}")