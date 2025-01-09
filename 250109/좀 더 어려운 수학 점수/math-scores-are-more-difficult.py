# A의 수학 점수, 영어 점수를 공백을 사이에 두고 입력한다
a = input().split()

a_math = int(a[0])
a_eng = int(a[1])

# B의 수학 점수, 영어 점수를 공백을 사이에 두고 입력한다
b = input().split()

b_math = int(b[0])
b_eng = int(b[1])

# 수학 점수가 더 높은 학생의 이름 출력
# a 수학 점수 > b 수학 점수인 경우 A 출력
# b 수학 점수 > a 수학 점수인 경우 B 출력
if a_math > b_math or (a_math == b_math and a_eng > b_eng):
    print('A')
else:
    print('B')

# 수학 점수가 같은 경우 영어 점수가 더 높은 학생의 이름 출력
# a 수학 점수 = b 수학 점수인 경우
    # a 영어 점수 > b 영어 점수인 경우 A 출력
    # b 영어 점수 > a 영어 점수인 경우 B 출력