from sys import stdin as s

# 정수의 개수인 N 입력
N = int(s.readline().rstrip())

# N개의 정수 입력
arr = list(map(int, s.readline().split()))

val_arr = []

# 서로 다른 두 개의 정수를 골랐을 때 차이의 최솟값
for i in range(N):
    for j in range(1, i):
        val = arr[i] - arr[j]
        if val > 0:
            val_arr.append(val)

print(min(val_arr))
