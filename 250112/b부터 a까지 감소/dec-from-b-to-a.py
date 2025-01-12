# 정수 a, b를 공백을 사이에 두고 입력한다
inp = input().split()

a = int(inp[0])
b = int(inp[1])

# b부터 a까지 1씩 감소하면서 공백을 사이에 두고 출력한다
for i in range (b, a - 1, -1):
    print(i, end = ' ')