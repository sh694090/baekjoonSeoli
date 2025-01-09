# 두 정수 a, b를 공백을 사이에 두고 입력한다
n = input().split()

a = int(n[0])
b = int(n[1])

# a >= b
if a >= b:
    print(1)
else:
    print(0)

# a > b
if a > b:
    print(1)
else:
    print(0)

# b >= a
if b >= a:
    print(1)
else:
    print(0)

# b > a
if b > a:
    print(1)
else:
    print(0)

# a == b
if a == b:
    print(1)
else:
    print(0)

# a != b
if a != b:
    print(1)
else:
    print(0)