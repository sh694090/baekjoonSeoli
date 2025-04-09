from sys import stdin as s

len_A, len_B = map(int, s.readline().split())
A = list(map(int, s.readline().split()))
B = list(map(int, s.readline().split()))

# B가 A의 연속 부분 수열인지 확인하는 법
# B의 첫번째 원소가 A에 있는지 확인
# 그리고 B의 원소를 차례대로 확인하면서 끝까지 A에 순서대로 들어있는지 확인
# 만약 끝까지 다 있으면 Yes 출력
# 아니면 No 출력

result = -1
if B[0] in A:
    A_start = A.index(B[0])
    for i in range(len_B):
        if B[i] == A[A_start + i]:
            # print(B[i], A[A_start + i])
            result = 1
        else:
            result = -1
else:
    result = -1

if result == 1:
    print("Yes")
else:
    print("No")