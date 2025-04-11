from sys import stdin as s

# 정수의 개수인 N 입력
N = int(s.readline().rstrip())

# N개의 정수 입력
arr = list(map(int, s.readline().split()))

# 주어진 정수들 중 최댓값의 위치 출력
# 만약 최댓값이 여러 개인 경우 가장 왼쪽에 있는 최댓값의 위치 출력
# 해당 최댓값의 위치보다 왼쪽에 있는 최댓값의 위치 출력
# 이 과정을 계속 반복해서 마지막에 1이 나오면 종료

# 최댓값 판별
max_index = N - 1
while max_index > 0:
    max_val = 0
    for cur_val in arr:
        if max_val < cur_val:
            max_val = cur_val
    max_index = arr.index(max_val)
    arr = arr[:max_index]
    print(max_index + 1, end = ' ')