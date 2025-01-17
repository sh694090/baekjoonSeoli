# 정수 a, b를 공백을 사이에 두고 한 줄에 입력한다
inp = input().split()

a = int(inp[0])
b = int(inp[1])

# a부터 b까지 숫자를 출력한다
# a에서 순회 시작해서 조건에 따라서 숫자가 바뀌고, 바뀐 해당 숫자가 b 넘지 않을 때까지 반복해야 함

i = a

while i <= b:
    print(i, end = " ")
    if i % 2 == 1:
        i *= 2
    else:
        i += 3