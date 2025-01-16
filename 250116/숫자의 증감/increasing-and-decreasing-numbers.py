# 문자 c, 숫자 n을 공백을 사이에 두고 한 줄에 입력한다
inp = input().split()

c = str(inp[0])
n = int(inp[1])

# c == 'A'인 경우
if c == 'A':
    for i in range(1, n + 1):
        print(i, end = " ")

# c == 'D'인 경우
else:
    for i in range(n, 0, -1):
        print(i, end = " ")