from sys import stdin as s

# N개의 정수가 주어졌을 때 2가 3번째 등장할 때 몇 번째 위치의 글자인지 출력

# 정수의 개수 N
N = int(s.readline().rstrip())

# N개의 수
arr = list(map(int, s.readline().split()))

# arr의 길이가 N이라는거잖아

# arr를 하나씩 순회하면서 2가 나오면 cnt += 1
cnt = 0
for i in range(N):
    if arr[i] == 2:
        cnt += 1
    if cnt == 3:
        break

print(i + 1)

