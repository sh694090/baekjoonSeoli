# 자연수 n을 입력한다
n = int(input())

# n >= 5인 경우 n * n의 결과를 출력한다
if n >= 5:
    print(n * n)
# n < 5인 경우 첫 번째 줄에는 n * n의 결과를, 두 번째 줄에는 tiny를 출력한다
if n < 5:
    print(n * n)
    print('tiny')