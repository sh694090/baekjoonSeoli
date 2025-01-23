# 숫자 10개를 한 줄에 하나씩 입력한다
# 3의 배수를 저장할 변수 하나랑, 5의 배수를 저장할 변수를 만들어야지
mult3 = 0
mult5 = 0
for _ in range(10):
    n = int(input())
    if n % 3 == 0 and n % 5 == 0:
        mult3 += 1
        mult5 += 1
    elif n % 3 == 0:
        mult3 += 1
    elif n % 5 == 0:
        mult5 += 1
print(mult3, mult5)