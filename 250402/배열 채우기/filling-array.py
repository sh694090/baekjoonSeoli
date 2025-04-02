from sys import stdin as s

arr = list(map(int, s.readline().split()))

# 중간에 0 나오면 입력 종료
# 입력된 정수들을 거꾸로 출력

# 리스트를 입력 받아서 얘네들을 하나씩 돌려서 0인지 판별
result = []
for elem in arr:
    if elem != 0:
        result.append(elem)
    else:
        break

for elem in result[::-1]:
    print(elem, end = " ")