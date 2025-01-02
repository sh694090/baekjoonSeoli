# 정수 a, b를 공백을 사이에 두고 입력한다
n = input().split()

a = int(n[0])
b = int(n[1])

# a < b인 경우 1 출력, 아닌 경우 0 출력
if a < b:
    print(1, end=" ")
else:
    print(0, end=" ")

# a = b인 경우 1 출력, 아닌 경우 0 출력
if a == b:
    print(1)
else:
    print(0)
# 두 숫자는 공백을 사이에 두고 출력함