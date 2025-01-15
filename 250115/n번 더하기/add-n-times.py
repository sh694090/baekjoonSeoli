# 정수 a, n을 공백을 사이에 두고 입력한다
inp = input()
arr = inp.split()

a = int(arr[0])
n = int(arr[1])

# 첫 번째 줄부터  a += n의 결과를 n줄 출력한다
for i in range(n):
    a += n
    print(a)