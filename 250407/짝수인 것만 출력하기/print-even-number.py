from sys import stdin as s

# N개의 원소 주어졌을 때, 주어진 원소 중 짝수인 값만 출력
# 그런데 이 짝수를 새로운 배열에 저장해서 출력

N = int(s.readline().rstrip())
arr = list(map(int, s.readline().split()))

even_list = []
for i in range(len(arr)):
    if arr[i] % 2 == 0:
        even_list.append(arr[i])
    else:
        continue

print(' '.join(map(str, even_list)))