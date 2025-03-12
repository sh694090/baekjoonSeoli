from sys import stdin as s

N = int(s.readline().rstrip())

# *의 개수
# 첫 번째 줄: 1
# 두 번째 줄: 3
# 세 번째 줄: 5
# 네 번째 줄: 7
# 다섯번째 줄: 9
# 2i - 1

# 첫 번째 줄: *
# 두 번째 줄: ***
# 세 번째 줄: *****

# 각 줄에 2i - 1만큼의 별 출력
for i in range(1, N + 1):
    for j in range(2 * i - 1):
        print("*", end = "")
    print()