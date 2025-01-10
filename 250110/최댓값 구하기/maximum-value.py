# 정수 a, b, c를 입력한다
a, b, c = input().split()

a = int(a)
b = int(b)
c = int(c)

# a, b 비교
if a > b and b > c:
    print(a)
elif b > a and a > c:
    print(b)
else:
    print(c)