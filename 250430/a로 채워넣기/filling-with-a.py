from sys import stdin as s

inp = s.readline().strip()

# 앞에서 2번째 원소, 뒤에서 2번째 원소를 문자 'a'로 대체한 결과 출력

arr = list(inp)

arr[1] = 'a'
arr[-2] = 'a'

result = ''.join(arr)

print(result)