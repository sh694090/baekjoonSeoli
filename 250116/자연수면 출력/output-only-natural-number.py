# 정수 a, b를 공백을 사이에 두고 한 줄에 입력한다
inp = input().split()

a = int(inp[0])
b = int(inp[1])

# a >= 1인 경우
if a >= 1:
    for _ in range(b):
        print(a, end = "")

# a <= 0인 경우
else:
    print(0)