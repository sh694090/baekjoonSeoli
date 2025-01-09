# 자연수 n을 입력한다
n = int(input())

# n이 홀수 and 3의 배수이면 true, 아니면 false 출력
# n이 짝수 and 5의 배수이면 true, 아니면 false 출력
if (n % 2 == 1 and n % 3 == 0) or (n % 2 == 0 and n % 5 == 0):
    print('true')
else:
    print('false')