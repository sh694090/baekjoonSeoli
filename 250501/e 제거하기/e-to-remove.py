from sys import stdin as s

# 가장 앞에 있는 e를 제거한 결과 출력
inp = list(s.readline().strip())

# e의 위치 출력하고 pop으로 없애
idx_e = inp.index('e')
inp.pop(idx_e)
result = ''.join(inp)
print(result)