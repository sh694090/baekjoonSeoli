from sys import stdin as s

# 첫번째 항과 두번째 항이 주어짐
p, pp = map(int, s.readline().split())

# 새로운 항 = 전 항 + 2 * 전전 항을 만족하도록 10번째 항까지 출력해라

arr = [p, pp]

for i in range(8):
    p, pp = pp, pp + 2 * p
    arr.append(pp)

print(" ".join(map(str, arr)))