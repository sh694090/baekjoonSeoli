from sys import stdin as s

# 정수 1개를 입력받아 배수를 차례로 출력하다가 5의 배수가 2번 출력되면 종료
# 배열 이용해서 해결해라...

N = int(s.readline().rstrip())
arr = []

for i in range(100):
    arr.append(N * (i + 1))

cnt = 0
for i in range(len(arr)):
    print(arr[i], end = " ")
    if arr[i] % 5 == 0:
        cnt += 1
    if cnt == 2:
        break