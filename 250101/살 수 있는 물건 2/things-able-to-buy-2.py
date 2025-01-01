# 가지고 있는 돈 n을 입력한다 (정수)
n = int(input())

# n >= 3000인 경우 book 출력
if n >= 3000:
    print("book")

# n >= 1000인 경우 mask 출력
elif n >= 1000:
    print("mask")

# n >= 500인 경우 pen 출력
elif n >= 500:
    print("pen")

# 그 이외의 경우 no 출력
else:
    print("no")