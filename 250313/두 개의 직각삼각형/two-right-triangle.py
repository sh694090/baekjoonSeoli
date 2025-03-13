from sys import stdin as s

N = int(s.readline().rstrip())

# N = 3인 경우
# 별 -> 공백 -> 별 이렇게 반복문을 돌리면 될듯

# i                별의 개수
# 0    ******        3  3        N - i  = 3
# 1    **  **        2  2        N - i  = 2
# 2    *    *        1  1        N - i  = 1

# N - i번 앞 뒤로 반복문 돌리면 될 듯

# i                공백의 개수
# 0    ******           0        i = 0
# 1    **vv**           2        2 * i = 2
# 2    *vvvv*           4        2 * i = 4

# 이렇게 별 가운데에 공백 출력

for i in range(N):
    for j in range(N - i):
        print("*", end = "")
    for j in range(2 * i):
        print(" ", end = "")
    for j in range(N - i):
        print("*", end = "")
    print()