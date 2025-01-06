# 정수 a, b를 공백을 사이에 두고 입력한다
n = input().split()

a = int(n[0])
b = int(n[1])

# a가 짝수인 경우 even, 홀수인 경우 odd 출력
if a % 2 == 0:
    print("even")
else:
    print("odd")
# b가 짝수인 경우 even, 홀수인 경우 odd 출력
if b % 2 == 0:
    print("even")
else:
    print("odd")