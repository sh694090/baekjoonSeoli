# 정수 a, b를 공백을 사이에 두고 입력한다
n = input().split()

a = int(n[0])
b = int(n[1])

# a에 b를 더한다
a += b

# b에 a를 더한다
b += a

# 위의 두 결과를 출력한다
print(a, b)