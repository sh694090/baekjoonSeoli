# 실수 a를 입력한다
a = float(input())

# 1.0 이상인 경우 High 출력
if a >= 1.0:
    print("High")
# 0.5 이상인 경우 Middle 출력
elif a >= 0.5:
    print("Middle")
# 이외의 경우 Low 출력
else:
    print("Low")