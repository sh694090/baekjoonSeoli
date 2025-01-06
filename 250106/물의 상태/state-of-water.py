# 정수 n을 입력한다
n = int(input())

# n < 0인 경우 'ice' 출력
if n < 0:
    print('ice')

# n >= 100인 경우 'vapor' 출력
elif n >= 100:
    print('vapor')

# 그 사이인 경우 'water' 출력
else:
    print('water')