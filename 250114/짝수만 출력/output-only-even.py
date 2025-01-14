# 정수 a, b를 입력한다
# a부터 b까지의 자연수 중 짝수만 출력하려면
# a부터 b까지 2씩 증가하면서 공백을 사이에 두고 출력하면 된다
inp = input().split()

a = int(inp[0])
b = int(inp[1])

i = a

while i <= b:
    print(i, end = ' ')
    i += 2