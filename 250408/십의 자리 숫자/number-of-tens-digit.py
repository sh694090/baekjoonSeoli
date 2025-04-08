from sys import stdin as s

# 세 자리 미만의 정수가 주어지다가 0이 주어지면
# 그 전까지 입력된 정수의 숫자들의 십의 자리 숫자가 각각 몇개인지
# 작은 수부터 출력

# 주어진 수를 배열로 받음
arr = list(map(int, s.readline().split()))

# 여기서 0이 주어지면 0을 제외하고 그 전까지의 숫자만 취급
new_arr = []
for elem in arr:
    if elem == 0:
        break
    else:
        new_arr.append(elem)

# 배열로 받은 이 수들의 십의 자리 숫자 출력
decimal_arr = []
for elem in new_arr:
    decimal_arr.append(elem // 10)

cnt_arr = [0] * 10
for elem in decimal_arr:
    cnt_arr[elem] += 1

for i in range(1, 10):
    cnt = cnt_arr[i]
    print(f"{i} - {cnt}")