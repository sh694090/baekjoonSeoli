from sys import stdin as s

# 알파벳으로 구성된 문자열의 길이 = L
# 오른쪽으로 한 글자씩 밀어서 출력 L회 반복
# = 맨 뒤의 글자가 맨 앞으로 이동을 L회 반복

inp = s.readline().strip()
L = len(inp)
print(inp)
for _ in range(L):
    inp = inp[-1:] + inp[0 : L - 1]
    print(inp)