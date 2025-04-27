from sys import stdin as s

N = int(s.readline().strip())

arr = []
# N줄에 걸쳐 N개의 문자열 주어짐
for _ in range(N):
    inp = s.readline().strip()
    arr.append(inp)

# 모든 문자열 길이의 합
len_sum = 0
for elem in arr:
    len_sum += len(elem)

# 'a'가 첫번째 문자로 몇번 나왔는가
cnt = 0
for elem in arr:
    if elem[0] == 'a':
        cnt += 1

print(len_sum, cnt)