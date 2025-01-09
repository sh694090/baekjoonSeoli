# 정수 a를 입력한다
a = int(input())

# a % 3 == 0 or a % 5 == 0인 경우 1 출력, 아니면 0 출력
if a % 3 == 0 or a % 5 == 0:
    print(1)
else:
    print(0)