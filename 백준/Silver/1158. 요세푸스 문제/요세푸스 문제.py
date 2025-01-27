from sys import stdin as s

N, K = map(int, s.readline().split())

# 처음 있는 사람들의 리스트
initial_list = []
for i in range (1, N + 1):
    initial_list += [i]

# 제거된 사람 리스트
delete_list = []

cur = 0

while len(initial_list) > 0:
    index = (cur + K - 1) % len(initial_list)

# 3번째 위치 = 2번 인덱스
    delete_list.append(initial_list[index])
    initial_list.pop(index)
    cur = index

print(f"<{', '.join(map(str, delete_list))}>")