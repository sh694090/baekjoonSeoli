from sys import stdin as s

# 정수 n이 주어지면 n을 두 번째 항으로 초기화, 첫 번째 항은 1로 초기화
# 3번째 항부터 전전항과 전 항을 더한 수로 채워나가다가 100을 넘길 때까지 출력
# 그래서 100을 넘기면 break하면 될 거같은데

# 이거 그냥 피보나치잔아

n = int(s.readline().rstrip())
pp = n
p = 1
arr = [1, n]

while True:
    p, pp = pp, p + pp
    arr.append(pp)
    if pp >= 100:
        break

print(" ".join(map(str, arr)))