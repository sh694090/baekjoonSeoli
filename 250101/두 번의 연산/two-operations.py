# 정수 a를 입력한다
a = int(input())

# a % 2 != 0인 경우 a = a + 3
if a % 2 != 0:
    a = a + 3

# a % 3 == 0인 경우 a = a / 3
if a % 3 == 0:
    a = int(a / 3)
    print(a)

else:
    print(a)