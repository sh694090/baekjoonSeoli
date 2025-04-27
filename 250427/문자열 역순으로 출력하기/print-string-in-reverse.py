from sys import stdin as s

arr = []

for _ in range(4):
    inp = s.readline().strip()
    arr.append(inp)

# arr의 원소를 거꾸로 출력
result = arr[::-1]

for elem in result:
    print(elem)