# 정수 b, a를 공백을 사이에 두고 입력한다
inp = input().split()

b = int(inp[0])
a = int(inp[1])

# b부터 a까지 홀수를 내림차순으로 공백을 사이에 두고 출력한다
for i in range (b, a - 1, -2):
    print(i, end = ' ')