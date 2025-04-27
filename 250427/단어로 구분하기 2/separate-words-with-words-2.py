from sys import stdin as s

# 공백을 포함한 10개의 문자열 입력
# 공백으로 구분해서 홀수 번째 문자만 출력

arr = tuple(s.readline().split())

for i in range(1, 11):
    if i % 2 != 0:
        print(arr[i - 1])
    else:
        continue

