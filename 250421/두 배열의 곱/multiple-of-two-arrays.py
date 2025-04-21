from sys import stdin as s

# 배열 선언과 동시에 입력받는게 더 좋아보이는데
arr1 = [list(map(int, s.readline().split())) for _ in range(3)]

while True:
    blank = s.readline().strip()
    if blank == "":
        break

arr2 = [list(map(int, s.readline().split())) for _ in range(3)]

result = [[0] * 3 for _ in range(3)]

for i in range(3):
    for j in range(3):
        elem = arr1[i][j] * arr2[i][j]
        result[i][j] = elem

for i in range(3):
    for j in range(3):
        print(result[i][j], end = " ")
    print()