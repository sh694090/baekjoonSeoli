# 정수 a, b를 한 줄에 공백을 사이에 두고 입력한다
number = input().split()

a = int(number[0])
b = int(number[1])

# a * b의 식과 결과를 출력한다
print(f"{a} * {b} = {a * b}")

# a / b의 식과 결과를 출력한다
print(f"{a} / {b} = {a // b}")