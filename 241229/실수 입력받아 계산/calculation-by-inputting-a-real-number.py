# 여러 줄로 실수 a, b를 입력받는다
a = input()
b = input()

# a, b를 실수로 바꿔준다
a = float(a)
b = float(b)

# 실수 a, b의 합을 소수점 아래 둘째자리까지 출력한다
print(f"{a + b:.2f}")