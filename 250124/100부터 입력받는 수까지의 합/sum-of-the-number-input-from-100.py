# 100 이하의 정수 n을 입력
n = int(input())

# n부터 100까지의 합 출력
sum_val = 0

for i in range(n, 101):
    sum_val += i
print(sum_val)