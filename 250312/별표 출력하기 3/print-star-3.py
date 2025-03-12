from sys import stdin as s

N = int(s.readline().rstrip())

# N = 3

# 별의 개수
# i
# 0    * * * * *        2 * (N - i) - 1 = 5
# 1      * * *          2 * (N - i) - 1 = 3
# 2        *            2 * (N - i) - 1 = 1

# 공백의 개수
# i
# 0    * * * * *        i = 0
# 1    v * * *          i = 1
# 2    v v *            i = 2
# 뒤쪽에 생기는 공백은 고려하지 않아도 됨

# 공백 먼저 출력하고 별 출력

for i in range(N):
    for j in range(i):
        print(" ", end = " ")
    for j in range(2 * (N - i) - 1):
        print("*", end =" ")
    print()