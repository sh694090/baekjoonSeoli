from sys import stdin as s

inp = list(s.readline().strip())

# 두번째 문자와 같은 문자 => 첫번째 문자로 바꿔서 출력

first = inp[0]
second = inp[1]

for i in range(len(inp)):
    if inp[i] == second:
        inp[i] = first

result = ''.join(inp)
print(result)