from sys import stdin as s

# 5행 3열 배열 입력
# 소문자로 주어진 애들을 대문자로 바꾸기
# A는 65
# a는 97

# 5행 3열의 배열을 어떻게 입력 받지

arr_2d = []
for _ in range(5):
    arr_1d = list(map(str, s.readline().split()))
    arr_2d.append(arr_1d)

for i in range(5):
    for j in range(3):
        arr_2d[i][j] = ord(arr_2d[i][j]) - 32

for i in range(5):
    for j in range(3):
        print(chr(arr_2d[i][j]), end = " ")
    print()