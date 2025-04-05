from sys import stdin as s

# N개 원소가 공백을 사이에 두고 입력
# N개의 원소를 각각 제곱해서 출력

N = int(s.readline().rstrip())
arr = list(map(int, s.readline().split()))
new_arr = [elem ** 2 for elem in arr]

for elem in new_arr:
    print(elem, end = " ")