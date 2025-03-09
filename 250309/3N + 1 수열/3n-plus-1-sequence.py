from sys import stdin as s

# N이 짝수 => 2로 나눔
# N이 홀수 => 3 곱하고, 1 더함

# 이 과정을 몇 번 반복해야 1이 되는지 출력
N = int(s.readline().rstrip())

cnt = 0

while True:
    if N == 1:
        break
    elif N % 2 == 0:
        N /= 2
        cnt += 1
    elif N % 2 != 0:
        N = N * 3 + 1
        cnt += 1

print(cnt)