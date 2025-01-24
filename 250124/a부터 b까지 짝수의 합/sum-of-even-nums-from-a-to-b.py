# 자연수 a, b를 한 줄에 공백을 사이에 두고 입력한다
inp = input().split()

a = int(inp[0])
b = int(inp[1])

sum_val = 0

# a부터 b까지 짝수의 합을 출력
for i in range(a, b + 1):
    if i % 2 == 0:
        sum_val += i
print(sum_val)