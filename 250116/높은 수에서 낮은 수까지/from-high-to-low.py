# 정수 a, b를 공백을 사이에 두고 한 줄에 입력한다
inp = input().split()

a = int(inp[0])
b = int(inp[1])

# a >= b인 경우
if a >= b:
    for i in range(a, b - 1, -1):
        print(i, end = " ")
# a < b인 경우
else:
    for i in range(b, a - 1, -1):
        print(i, end = " ")