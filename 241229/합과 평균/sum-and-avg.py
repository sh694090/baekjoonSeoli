# 정수 a, b를 공백을 사이에 두고 입력한다
n = input().split()

a = int(n[0])
b = int(n[1])

# 정수 a, b의 합과 평균을 소수 첫째 자리까지 공백을 사이에 두고 출력한다
print(f"{a + b} {(a + b) / 2:.1f}")