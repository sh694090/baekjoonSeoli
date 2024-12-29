# 정수 a, b를 공백을 사이에 두고 입력한다
n = input().split()

a = int(n[0])
b = int(n[1])

# (a + b) / (a - b)의 결과를 반올림해 소수점 둘째 자리까지 출력한다
result = (a + b) / (a - b)

print(f"{result:.2f}")