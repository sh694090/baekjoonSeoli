from sys import stdin as s

# N, M 공백을 사이에 두고 입력
# 두 번째 줄에 N개만큼 정수 입력

N, M = map(int, s.readline().split())

arr = list(map(int, s.readline().split()))

# M이 등장하는 횟수 출력
cnt = arr.count(M)
print(cnt)
