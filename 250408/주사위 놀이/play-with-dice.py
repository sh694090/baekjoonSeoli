from sys import stdin as s

# 주사위 10번 던짐
# 그러면 결과는 10번 출력됨
arr = list(map(int, s.readline().split()))

# "주사위 숫자 - 나온 횟수" 형식으로 출력

cnt_arr = [0] * 7
for elem in arr:
    cnt_arr[elem] += 1

for i in range(1, 7):
    cnt = cnt_arr[i]
    print(f"{i} - {cnt}")
        