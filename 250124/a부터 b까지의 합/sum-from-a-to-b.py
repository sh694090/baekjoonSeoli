# 첫 번째 줄에 정수 a, b를 공백을 사이에 두고 입력
inp = input().split()

a = int(inp[0])
b = int(inp[1])

sum_val = 0

# a부터 b까지의 합 출력
for i in range(a, b + 1):
    sum_val += i
print(sum_val)