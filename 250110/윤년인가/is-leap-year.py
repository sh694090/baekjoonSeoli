# 자연수 y를 입력한다
y = int(input())

# y가 4로 나눠지면 true, 아니면 false
# 100으로 나누어 떨어지고 400으로 나누어 떨어지지 않는 해는 false 출력
if y % 4 == 0:
    if (y % 100 == 0 and y % 400 != 0):
        print('false')
    else:
        print('true')
else:
    print('false')