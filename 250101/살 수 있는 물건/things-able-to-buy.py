# 가지고 있는 돈 n 입력 (정수)
n = int(input())

# n >= 3000인 경우 book 출력
if n >= 3000:
    print("book")

# n >= 1000인 경우 mask 출력
elif n >= 1000:
    print("mask")

# 이외의 경우 no 출력
else:
    print("no")