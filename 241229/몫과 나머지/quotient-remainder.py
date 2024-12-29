# 정수 a, b를 공백을 사이에 두고 입력한다
n = input().split()

a = int(n[0])
b = int(n[1])

# a를 b로 나눈 몫과 나머지를 출력한다
print(f"{int(a / b)}...{a % b}")