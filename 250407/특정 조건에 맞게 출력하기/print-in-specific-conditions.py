from sys import stdin as s

# 정수가 차례로 주어지다가 0이 주어지면 0을 제외하고, 그때까지 주어진 정수를 차례로 출력
# 그 수가 홀수이면 3을 더하고, 짝수이면 2로 나눈 몫 출력

arr = list(map(int, s.readline().split()))

for i in range(len(arr)):
    if arr[i] == 0:
        break
    elif arr[i] % 2 == 0:
        print(arr[i] // 2, end = " ")
    elif arr[i] % 2 != 0:
        print(arr[i] + 3, end = " ")