# 정수 a, b를 공백을 사이에 두고 입력한다
inp = input().split()

a = int(inp[0])
b = int(inp[1])

# a 이상 b 이하의 홀수를 공백을 두고 출력한다 (a ~ b + 1의 숫자를 2 간격으로 출력)
for i in range (a, b + 1, 2):
    print(i, end = ' ')