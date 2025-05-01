from sys import stdin as s

# 자연수 5개 입력
# 해당 자연수에 해당하는 문자 출력
inp = list(map(int, s.readline().split()))

for i in range(5):
    result = chr(inp[i])
    print(result, end = " ")