from sys import stdin as s

N = int(s.readline().rstrip())

# 1부터 N까지 1씩 증가하면서 N을 나눴을 때 나머지가 0일 때 약수
# 근데 자기 자신을 제외해야하기 때문에 range를 (1, N)으로 잡아서 N 이전까지 나누도록 하기
# 그리고 그렇게 나온 값을 하나씩 더해서 N이 나오면 P, 아니면 N 출력

result = 0

for i in range(1, N):
    if N % i == 0:
        result += i

if result == N:
    print('P')
else:
    print('N')