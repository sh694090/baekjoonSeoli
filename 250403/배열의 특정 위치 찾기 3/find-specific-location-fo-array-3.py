from sys import stdin as s

# 정수 차례로 주어지다가 0이 나오면 0 앞의 3개의 수 더해서 출력
# 그러면 0 주어지기 전까지의 수를 새로운 리스트에 넣어야 하겠고만

arr = list(map(int, s.readline().split()))

new_arr = []
for i in range(len(arr)):
    if arr[i] == 0:
        break
    else:
        new_arr.append(arr[i])

sum = new_arr[-1] + new_arr[-2] + new_arr[-3]
print(sum)