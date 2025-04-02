from sys import stdin as s

# 정수 10개 차례로 주어짐
# 0이 나오기 전까지 주어진 정수 중 2의 배수 개수, 합계 출력

arr = list(map(int, s.readline().split()))

sum = 0
cnt = 0

for elem in arr:
    if elem != 0 and elem % 2 == 0:
        sum += elem
        cnt += 1
    elif elem != 0:
        continue
    else:
        break

print(cnt, sum)