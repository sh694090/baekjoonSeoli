from sys import stdin as s

# 정수 10개를 입력받아서 그 합과 평균 출력
# 0이 나오면 10개 입력이 완료되지 않았어도 그때까지 입력된 합, 평균 출력
# 0 입력된 경우 0 제외한 합, 평균 계산

arr = list(map(int, s.readline().split()))

sum = 0
cnt = 0

for elem in arr:
    if elem != 0:
        sum += elem
        cnt += 1
    else:
        break

avg = sum / cnt

print(sum, f"{avg:.1f}")