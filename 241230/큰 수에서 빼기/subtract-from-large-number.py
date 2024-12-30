# 정수 a, b를 공백을 사이에 두고 한줄로 입력한다
n = input().split()

a = int(n[0])
b = int(n[1])

# a > b인 경우 a - b의 결과를 출력한다
if a >= b:
    print(a - b)
# a < b인 경우 b - a의 결과를 출력한다
if a < b:
    print(b - a)