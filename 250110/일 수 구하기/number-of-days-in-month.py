# 자연수 n을 입력한다
n = int(input())

# 2월은 28 출력
# 1, 3, 5, 7, 8, 10, 12월은 31출력
# 4, 6, 9, 11월은 30 출력
if n == 2:
    print(28)
elif n == 4 or n == 6 or n == 9 or n == 11:
    print(30)
else:
    print(31)