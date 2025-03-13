from sys import stdin as s

N = int(s.readline().rstrip())

# N = 3인 경우

# i                     별의 개수
# 0        *                1
# 1      * * *              3
# 2    * * * * *            5

# 별은 2 * i - 1개

# i                     공백의 개수
# 0   v v *                 2
# 1   v * * *               1
# 2   * * * * *             0

# 공백은 N - 1 - i개

# 공백 먼저 출력하고 별 출력

for i in range(N):
    for j in range(1, N - i):
        print(" ", end = " ")
    for j in range(2 * i + 1):
        print("*", end = " ")
    print()