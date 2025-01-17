# 자연수 n을 입력한다
n = int(input())
# 1부터 n까지 반복문으로 순회한다
for i in range(1, n + 1):
    if (i % 2 == 0) or (i % 3 == 0):
        print(1, end = " ")
    else:
        print(0, end = " ")
# 해당 수가 2의 배수 or 3의 배수이면 1 출력
# 이외의 경우에는 0 출력
# 이 1과 0을 공백을 사이에 두고 한 줄로 출력