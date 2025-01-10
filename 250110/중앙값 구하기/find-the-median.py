# 정수 a, b, c를 공백을 두고 입력한다 (a, b, c는 모두 다르다)
inp = input().split()

a = int(inp[0])
b = int(inp[1])
c = int(inp[2])

# a > b일 때 c가 a보다 크면 중간값은 a, c가 a보다 작으면 중간값은 
if a > b:
    if c > a:
        print(a)
    else:
        if b > c:
            print(b)
        else:
            print(c)
else:
    if c > b:
        print(b)
    else:
        if c > a:
            print(c)
        else:
            print(a)
