# 정수 a, b, c를 입력한다
a, b, c = input().split()

a = int(a)
b = int(b)
c = int(c)

# a가 세 정수 중 가장 작으면 1 출력, 아니면 0 출력
if a <= b and a <= c:
    print(1, end = ' ')
else:
    print(0, end = ' ')

# 정수 a, b, c가 모두 같으면 1 출력, 아니면 0 출력
if a == b == c:
    print(1)
else:
    print(0)