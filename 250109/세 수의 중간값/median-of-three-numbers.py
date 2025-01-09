# 정수 a, b, c를 공백을 사이에 두고 입력한다
a, b, c = input().split()

a = int(a)
b = int(b)
c = int(c)

# b > a and b < c인 경우 1 출력
if b > a and b < c:
    print(1)

# 아닌 경우 0 출력
else:
    print(0)