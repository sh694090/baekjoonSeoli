# cnt번의 연산했을 때 처음으로 1000 이상이 되는 cnt의 값 출력

# N이 짝수 => N * 3 + 1
# N이 홀수 => N * 2 + 2

from sys import stdin as s

N = int(s.readline().rstrip())

cnt = 0
while N < 1000:
    if N % 2 == 0:
        N = N * 3 + 1
        cnt += 1
    elif N % 2 != 0:
        N = N * 2 + 2
        cnt += 1
print(cnt)