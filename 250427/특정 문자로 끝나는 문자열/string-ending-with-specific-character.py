from sys import stdin as s

# 10개의 문자열
arr = []
for _ in range(10):
    inp = s.readline().strip()
    arr.append(inp)

# 하나의 문자
alp = s.readline().strip()

# 주어진 문자로 끝나는 문자열 출력
result = []
for elem in arr:
    if elem[-1] == alp:
        result.append(elem)

if not result:
    print("None")
else:
    for elem in result:
        print(elem)
    