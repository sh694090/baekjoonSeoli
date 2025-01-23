# 10개의 수를 한 줄에 하나씩 입력
cnt = 0
for _ in range (10):
    n = int(input())
    if n % 2 == 1:
        cnt += 1
print(cnt)