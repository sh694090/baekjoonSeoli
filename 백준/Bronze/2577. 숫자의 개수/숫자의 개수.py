# 숫자의 개수를 저장할 배열을 만들고 기본값을 0으로 초기화한다
number_count = [0] * 10

# A * B * C를 구한다
A = int(input())
B = int(input())
C = int(input())

result = A * B * C

for number in str(result):
    index = int(number)
    number_count[index] += 1

for i in range(10):
    print(number_count[i])
    i += 1