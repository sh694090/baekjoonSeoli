from sys import stdin as s

# 두 정수 A, B가 주어짐
# A // B의 결과를 A에 계속해서 저장
# A가 1 이하가 되기 전까지 이 과정 반복
# 각 나눗셈 연산마다 나온 나머지가 등장한 횟수 제곱해서 그 합 출력
# 와 이건 뭐 문제를 이해하는거부터가 에바인데

A, B = map(int, s.readline().split())

remainder_arr = []
while A > 1:
    remainder_arr.append(A % B)
    A = A // B

cnt_arr = [0] * 11
for elem in remainder_arr:
    cnt_arr[elem] += 1

result = 0
for i in range(len(cnt_arr)):
    result += cnt_arr[i] ** 2

print(result)
