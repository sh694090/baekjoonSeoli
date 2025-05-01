from sys import stdin as s

# 앞에서 2번째 원소, 뒤에서 2번째 원소 제거한 후의 문자열
inp = list(s.readline().strip())

inp.pop(1)
inp.pop(-2)

result = ''.join(inp)
print(result)