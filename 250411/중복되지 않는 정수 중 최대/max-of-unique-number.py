from sys import stdin as s

# 원소의 개수인 N 입력
N = int(s.readline().rstrip())

# N개의 정수 공백 사이에 두고 주어짐
arr = list(map(int, s.readline().split()))

max_val = -1
for cur_val in arr:
    if max_val < cur_val:
        cnt = 0
        for elem in arr:
            if cur_val == elem:
                cnt += 1

        if cnt == 1:
            max_val = cur_val

print(max_val)