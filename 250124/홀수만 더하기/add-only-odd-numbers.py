# 정수 n 입력 (1 <= n <= 10)
n = int(input())

sum_val = 0
# n줄에 걸쳐 정수 하나씩 입력
for _ in range(n):
    inp = int(input())
    if inp % 2 != 0 and inp % 3 == 0:
        sum_val += inp
print(sum_val)
# 주어지는 n개의 정수는 모두 1 <= 정수 <= 100
# 이 정수들의 합을 구해라
# 홀수이면서 3의 배수여야하는구나