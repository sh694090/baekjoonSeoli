# 정수인 점수 n을 입력한다
n = int(input())

# 90점 이상인 경우 A
if n >= 90:
    print("A")

# 80점 이상인 경우 B
elif n >= 80:
    print("B")

# 70점 이상인 경우 C
elif n >= 70:
    print("C")

# 60점 이상인 경우 D
elif n >= 60:
    print("D")

# 60점 미만인 경우(위 경우 이외의 경우) F
else:
    print("F")