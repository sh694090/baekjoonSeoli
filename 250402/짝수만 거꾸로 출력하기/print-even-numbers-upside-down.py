from sys import stdin as s

# 주어진 정수에서 짝수만 역순으로 출력

N = int(s.readline().rstrip())
arr = list(map(int, s.readline().split()))

even = []
for elem in arr:
    if elem % 2 == 0:
        even.append(elem)
    else:
        continue

for elem in even[::-1]:
    print(elem, end = " ")