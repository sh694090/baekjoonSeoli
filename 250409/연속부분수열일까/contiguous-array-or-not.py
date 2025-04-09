from sys import stdin as s

len_A, len_B = map(int, s.readline().split())
A = list(map(int, s.readline().split()))
B = list(map(int, s.readline().split()))

# B가 A의 연속 부분 수열인지 확인하는 법
# B의 첫번째 원소가 A에 있는지 확인
# 그리고 B의 원소를 차례대로 확인하면서 끝까지 A에 순서대로 들어있는지 확인
# 만약 끝까지 다 있으면 Yes 출력
# 아니면 No 출력

# A_start는 A에서 B[0]가 있는 인덱스를 저장한 리스트
A_start = []
result = -1
for a in A:
    if a == B[0]:
        A_start.append(A.index(a))
# print(A_start)

# start_A의 모든 요소를 하나씩 순회
# A 중 B[0]가 있는 인덱스 저장
for i in range(len(A_start)):
    # 처음에 A[start_A[0]]에 B[0]이 있지
    if B[0] == A[A_start[i]]:
        # A_start = A.index(B[0])
        for j in range(len_B):
            if B[j] == A[A_start[i] + j]:
             # print(B[i], A[A_start + i])
              result = 1
            else:
             # print(B[i], A[A_start + i])
                result = -1
    else:
        result = -1

if result == 1:
    print("Yes")
else:
    print("No")