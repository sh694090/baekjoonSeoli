from sys import stdin as s

# 원소의 개수 N 입력
N = int(s.readline().rstrip())

# N개의 정수 입력
arr = list(map(int, s.readline().split()))

# 최솟값
min_val = min(arr)

# 최솟값의 개수
cnt = 0
for i in range(N):
    if arr[i] == min_val:
        cnt += 1

print(min_val, cnt)