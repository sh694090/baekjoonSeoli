# 출석번호를 입력한다 (정수)
n = int(input())

# 출석번호 == 1인 경우 John 출력
if n == 1:
    print("John")

# 출석번호 == 2인 경우 Tom 출력
elif n == 2:
    print("Tom")

# 출석번호 == 3인 경우 Paul 출력
elif n == 3:
    print("Paul")

# 이외의 경우 Vacancy 출력
else:
    print("Vacancy")