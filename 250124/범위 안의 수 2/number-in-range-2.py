# 한 줄에 하나씩 정수 입력
sum_val = 0
average_val = 0
cnt = 0

for _ in range(10):
    inp = int(input())
    if inp >= 0 and inp <= 200:
        sum_val += inp
        cnt += 1
average_val = sum_val / cnt
print(sum_val, f"{average_val:.1f}")
# 이 정수들 중 0 이상 200이하의 합, 평균 공백을 사이에 두고 한 줄에 출력