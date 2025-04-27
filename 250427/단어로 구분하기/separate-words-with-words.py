from sys import stdin as s

# 공백을 포함한 10개의 문자열
# 공백으로 나눠서 출력

arr = tuple(s.readline().split())

for elem in arr:
    print(elem)