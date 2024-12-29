# 실수 a, b, c를 한 줄씩 입력받는다
a = input()
b = input()
c = input()

# a, b, c를 실수형으로 형변환을 한다
a = float(a)
b = float(b)
c = float(c)

# 각 변수를 소수 셋째자리까지 출력한다
print(f"{a:.3f}")
print(f"{b:.3f}")
print(f"{c:.3f}")