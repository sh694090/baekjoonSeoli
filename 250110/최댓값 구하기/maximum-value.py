# 정수 a, b, c를 입력한다
a, b, c = input().split()

a = int(a)
b = int(b)
c = int(c)

if a >= b:
    if a >= c:
        print(a)
    else:
        print(c)
else:
    if b >= c:
        print(b)
    else:
        print(c)