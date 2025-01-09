# 정수 a를 입력한다
a = int(input())

# a % 13 == 0 또는 a % 19 == 0인 경우 'True' 출력, 아니면 'False' 출력
if a % 13 == 0 or a % 19 == 0:
    print('True')
else:
    print('False')