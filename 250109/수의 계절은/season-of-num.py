# 정수 m을 입력한다
m = int(input())

# 3 <= m <= 5이면 Spring 출력
if m >= 3 and m <= 5:
    print('Spring')

# 6 <= m <= 8이면 Summer 출력
elif m >= 6 and m <= 8:
    print('Summer')

# 9 <= m <= 11이면 Fall 출력
elif m >= 9 and m <= 11:
    print('Fall')

# m <= 2 and m >= 12이면 Winter 출력
else:
    print('Winter')