from sys import stdin as s

start, end = map(int, s.readline().split())

# start 이상 end 이하인 정수 중 약수가 3개인 수 구해라

cnt = 0
for i in range(start, end + 1):
    fac = 0
    for j in range(1, i + 1):
        if i % j == 0:
            fac += 1
    if fac == 3:
        cnt += 1
print(cnt)