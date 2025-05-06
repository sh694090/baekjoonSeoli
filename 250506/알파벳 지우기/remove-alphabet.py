from sys import stdin as s

# 알파벳과 숫자로 이루어진 문자열 2개 주어짐

A = list(s.readline().strip())
B = list(s.readline().strip())

# 알파벳을 제외하고 남은 숫자만 차례로 이어만든 수
# 주어진 두 개의 숫자 더한 결과

A_digit = []
for i in range(len(A)):
    if A[i].isdigit() != True:
        continue
    else:
        A_digit.append(A[i])

B_digit = []
for i in range(len(B)):
    if B[i].isdigit() != True:
        continue
    else:
        B_digit.append(B[i])

A = ''.join(A_digit)
B = ''.join(B_digit)

result = int(A) + int(B)
print(result)