# A의 수학점수, 영어점수를 공백을 사이에 두고 입력한다
a_math, a_eng = input().split()

a_math = int(a_math)
a_eng = int(a_eng)

# B의 수학점수, 영어점수를 공백을 사이에 두고 입력한다
b_math, b_eng = input().split()

b_math = int(b_math)
b_eng = int(b_eng)

# A의 수학점수 > B의 수학점수 and A의 영어점수 > B의 영어점수
# true이면 1 출력, false이면 0 출력
if (a_math > b_math) and (a_eng > b_eng):
    print(1)
else:
    print(0)