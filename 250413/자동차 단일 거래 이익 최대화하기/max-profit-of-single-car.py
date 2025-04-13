from sys import stdin as s

# N 입력
N = int(s.readline().rstrip())

# N년 간 각 해의 자동차 가격
price_arr = list(map(int, s.readline().split()))

revenue_arr = []

for i in range(N):
    for j in range(1, i):
        revenue_arr.append(price_arr[i] - price_arr[j])

if revenue_arr and max(revenue_arr) > 0:
    print(max(revenue_arr))
else:
    print(0)