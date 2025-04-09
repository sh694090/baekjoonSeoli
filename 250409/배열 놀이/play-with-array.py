from sys import stdin as s

# 두 정수 N, Q 입력
N, Q = map(int, s.readline().split())

# N개의 원소 값이 차례대로 공백으로 구분해 입력
arr = list(map(int, s.readline().split()))

# Q개의 줄에 걸쳐 Q개의 질의 하나씩 입력
for i in range(Q):
    q_arr = list(map(int, s.readline().split()))
    q_num = q_arr[0]
    if q_num == 1:
        print(arr[q_arr[1] - 1])
    elif q_num == 2:
        # arr에서 값이 q_arr[1]의 값과 같은 원소를 찾아서 그거의 index + 1 출력
        # 만약 같은 값이 없다면 0 출력
        if q_arr[1] in arr:
            print(arr.index(q_arr[1]) + 1)
        else:
            print(0)
    elif q_num == 3:
        # q_arr[1]번째 원소 ~ q_arr[2]번째 원소의 값을 공백으로 구분해서 출력
        for i in range(q_arr[1] - 1, q_arr[2]):
            print(arr[i], end = " ")
        print()