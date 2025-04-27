from sys import stdin as s

# 공백을 기준으로 나뉘는 10개의 문자열 입력
# 입력 순서의 반대로 출력

arr = tuple(s.readline().split())
result = arr[::-1]

for elem in result:
    print(elem)