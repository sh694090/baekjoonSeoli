# 자연수 n을 입력한다
n = int(input())

# n 이상의 n의 배수 중 작은 수 5개를 출력한다
# 그러면 n을 간격으로 n * 5 + 1까지의 값을 출력하면 될거같은디
for i in range (n, n * 5 + 1, n):
    print(i, end = ' ')