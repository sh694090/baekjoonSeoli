from sys import stdin as s

# 원소의 개수
N = int(s.readline().rstrip())

# N개의 원소가 공백을 사이에 두고 주어짐
arr = list(map(int, s.readline().split()))

# i번째 줄이 i가 몇번 주어졌는지 출력
# 그러면 반복문이 1 ~ N + 1까지 돌면 되겠지

# 각 줄에 그 줄에 해당하는 숫자가 나오면 +1 하면 될거같은데
# 해당 줄은 어떻게 구해야하는거지
# 그냥 배열에 넣어두고 하나씩 돌려서 출력하면 되는건가

count_arr = [0] * 10

for elem in arr:
    count_arr[elem] += 1

for i in range(1, 10):
    cnt = count_arr[i]
    print(count_arr[i])
        