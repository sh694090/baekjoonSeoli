from sys import stdin as s

# 원소의 개수인 N 입력
N = int(s.readline().rstrip())

# N개의 정수 공백을 사이에 두고 입력
arr = list(map(int, s.readline().split()))

# 내림차순 정렬 시 첫 번째와, 두 번째 정수 출력
# 가장 큰 정수, 그 다음으로 큰 정수 출력하라는거지
# max_value 구하고 그걸 리스트에서 삭제하고 그 다음에 다시 arr의 max_value 구하면 되지 않나?

first = max(arr)
first_index = arr.index(first)
arr.pop(first_index)
second = max(arr)

# second = max(new_arr)

print(first, second)