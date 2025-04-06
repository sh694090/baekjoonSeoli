from sys import stdin as s

# 10 미만의 정수 2개 주어짐
# 순서대로 첫번째 항, 두번째 항
# 세 번째 항부터는 전전 항 + 전 합
# 그 합의 1의 자리로 차례로 10개 출력

a, b = map(int, s.readline().split())

print(a, end = " ")

for i in range(9):
    a, b = b, a + b
    print(a % 10, end = " ")