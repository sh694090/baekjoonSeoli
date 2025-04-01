from sys import stdin as s

inp = list(map(int, s.readline().split()))

# 정수 10개 주어짐
# 250 이상의 정수 나오는 순간 마지막으로 주어진 수 제외하고 주어진 모든 정수들의 합계, 평균 계산
# 250 이상의 정수 없는 경우 10개의 합계, 평균 계산

sum = 0
for i in range(len(inp)):
    if inp[i] < 250:
        sum += inp[i]
    else:
        break
    
    avg = sum / (i + 1)

print(sum, f"{avg:.1f}")