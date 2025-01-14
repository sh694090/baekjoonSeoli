# 두 정수 b, a를 공백을 사이에 두고 입력한다
inp = input().split()

a = int(inp[1])
b = int(inp[0])

# 정수 b부터 a까지의 자연수 중 짝수만 공백을 사이에 두고 내림차순으로 출력한다
i = b

while i >= a:
    print(i, end = ' ')
    i -= 2