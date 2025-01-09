# 실수 a를 입력한다
a = float(input())

# 실수 b를 입력한다
b = float(input())

# a, b >= 1.0인 경우 'High' 출력
if a >= 1.0 and b >= 1.0:
    print('High')

# a, b >= 0.5인 경우 'Middle' 출력
elif a >= 0.5 and b >= 0.5:
    print('Middle')

# 위의 경우 모두 아니면 'Low' 출력
else:
    print('Low')