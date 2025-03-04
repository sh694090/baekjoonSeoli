from sys import stdin as s

N = int(s.readline().rstrip())

# N을 1, 2, 3, ...으로 나누었을 때 1 이하가 될 때까지 나눈 횟수 구하기
# 나눈 횟수 (출력할 변수)
cnt = 0
quo = N

# 예시) N = 50
# 50을 1로 나눔
# quo = 50
# cnt += 1

# quo = 50을 2로 나눔
# quo = 25
# cnt += 1

# quo = 25를 3으로 나눔
# quo = 8
# cnt += 1

# quo = 8을 4로 나눔
# quo = 2
# cnt += 1

# quo = 2를 5로 나눔
# quo = 0
# cnt += 1
# 그러면 반복문 탈출하고 cnt = 5 출력

# i는 1부터 하나씩 증가 (조건 만족할 때까지 계속 증가) => 그럼 while문을 써야하나
i = 1
while quo / i >= 1:
    quo /= i
    i += 1

print(i)