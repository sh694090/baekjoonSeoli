# 첫 번째 줄에 성별에 해당하는 숫자를 입력한다
sex = int(input())

# 두 번째 줄에는 자연수인 나이를 입력한다
age = int(input())

# 성별이 0인 경우
    # 나이가 19세 이상인 경우 MAN 출력
    # 아닌경우 BOY 출력
if sex == 0:
    if age >= 19:
        print('MAN')
    else:
        print('BOY')
# 성별이 1인 경우
    # 나이가 19세 이상인 경우 WOMAN 출력
    # 아닌경우 GIRL 출력
else:
    if age >= 19:
        print('WOMAN')
    else:
        print('GIRL')