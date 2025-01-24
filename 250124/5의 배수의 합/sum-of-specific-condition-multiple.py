# 정수 a, b를 한 줄에 공백을 사이에 두고 입력
# a부터 b의 수 중 5의 배수인 수를 모두 더한 값 출력
# a < b일 수도 있고 a > b일 수도 있다
inp = input().split()

# 입력된 수 중 더 작은 숫자를 a, 큰 숫자를 b에 넣음
if int(inp[0]) <= int(inp[1]):
    a = int(inp[0])
    b = int(inp[1])
else:
    a = int(inp[1])
    b = int(inp[0])
sum_val = 0

for i in range(a, b + 1):
    if i % 5 == 0:
        sum_val += i
print(sum_val)