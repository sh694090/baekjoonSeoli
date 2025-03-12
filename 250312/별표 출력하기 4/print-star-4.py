from sys import stdin as s

N = int(s.readline().rstrip())

# N = 5

# i
# 0          *****    처음에는 별 5개
# 1          ****     1개 감소
# 2          ***      1개 감소
# 3          **       1개 감소
# 4          *        1개 감소
# 5          **       1개 증가
# 6          ***      1개 증가
# 7          ****     1개 증가
# 8          *****    1개 증가

# i가 4 이하까지는 1개씩 감소, 이후부터는 1개씩 증가
# cnt = N
# i < cnt인 경우 cnt -= 1
# 그 이외에는 cnt += 1

cnt = N
for i in range(2 * N - 1):
    for j in range(cnt):
        print("*", end = " ")
    print()

    if i < N - 1:
        cnt -= 1
    else:
        cnt += 1

# i = 4
# cnt = 
# 