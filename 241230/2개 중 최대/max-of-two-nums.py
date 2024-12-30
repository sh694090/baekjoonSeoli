# 정수 a, b를 공백을 사이에 두고 입력한다
n = input().split()

a = int(n[0])
b = int(n[1])

# a < b인 경우 b 출력, a > b인 경우 a 출력
result = a if a >= b else b
print(result)