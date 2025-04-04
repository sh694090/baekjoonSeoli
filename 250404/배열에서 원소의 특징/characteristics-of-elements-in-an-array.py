from sys import stdin as s

# 배열의 원소 10개 입력
# 원소 중 3의 배수가 처음으로 등장하는 부분의 바로 앞 원소 출력

arr = list(map(int, s.readline().split()))

for i in range(len(arr)):
    if arr[i] % 3 == 0:
        print(arr[i - 1])
        break
