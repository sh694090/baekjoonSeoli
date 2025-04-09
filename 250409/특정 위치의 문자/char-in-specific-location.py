from sys import stdin as s

# 6개의 문자 배열
arr = ['L', 'E', 'B', 'R', 'O', 'S']

# 입력받은 문자
inp = s.readline().rstrip()

if inp in arr:
    print(arr.index(inp))
else:
    print("None")