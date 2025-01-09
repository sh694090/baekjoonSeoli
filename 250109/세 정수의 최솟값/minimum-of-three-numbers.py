# 정수 a, b, c를 공백을 사이에 두고 입력한다
a, b, c = input().split()

a = int(a)
b = int(b)
c = int(c)

# a <= b and a <= c인 경우 최솟값은 a
if a <= b and a <= c:
    print(a)
    
# b <= a and b <= c인 경우 최솟값은 b
elif b <= a and b <= c:
    print(b)

# 그 외의 경우 최솟값은 c
else:
    print(c)