# 정수 h, w를 공백을 사이에 두고 입력한다
n = input().split()

h = int(n[0])
w = int(n[1])

# 체질량 지수인 정수 b를 계산한다
b = int((10000 * w) / (h * h))

# 비만이 아닌 경우 b를 출력한다
if b < 25:
    print(b)
# 비만인 경우 첫 번째 줄에 b를, 두 번째 줄에 Obesity를 출력한다
if b >= 25:
    print(b)
    print('Obesity')