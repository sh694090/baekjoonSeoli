# 정수 a, b, c를 공백을 두고 입력한다
n = input().split()

a = int(n[0])
b = int(n[1])
c = int(n[2])

# 정수 a, b, c의 합을 출력한다
addition = a + b + c

print(addition)

# 정수 a, b, c의 평균을 출력한다
average = int(addition / len(n))

print(average)

# 정수 a, b, c의 합에서 평균을 빼서 출력한다
result = addition - average

print(result)