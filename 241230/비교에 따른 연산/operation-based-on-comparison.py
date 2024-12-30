# 정수 a, b를 공백을 사이에 두고 입력한다
n = input().split()

a = int(n[0])
b = int(n[1])

# a > b인 경우 a * b의 결과 출력
if a > b:
    print(a * b)
# 나머지 경우 b // a의 결과 출력
else:
    print(b // a)