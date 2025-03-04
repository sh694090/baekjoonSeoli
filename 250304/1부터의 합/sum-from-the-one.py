from sys import stdin as s

N = int(s.readline().rstrip())

sum = 0

for i in range(1, 101):
    sum += i
    # sum이 N 이상인가?
    if sum >= N:
        print(i)
        break
    # 아니면 계속 반복문 돌기
    # N 이상이면 break하고 i 출력
