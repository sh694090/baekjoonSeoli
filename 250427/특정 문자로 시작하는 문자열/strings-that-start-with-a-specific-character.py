from sys import stdin as s

N = int(s.readline().strip())

arr = []
for _ in range(N):
    inp = s.readline().strip()
    arr.append(inp)

alp = s.readline().strip()

# 이 알파벳으로 시작하는 문자열의 개수
cnt = 0
len_sum = 0
for elem in arr:
    if elem[0] == alp:
        cnt += 1
        len_sum += len(elem)

len_avg = len_sum / cnt
print(cnt, f"{len_avg:.2f}")
