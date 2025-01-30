from sys import stdin as s
K = int(s.readline().rstrip())

result = []

for _ in range (K):
    inp = int(s.readline().rstrip())

    if inp == 0:
        result.pop()
    else:
        result += [inp]
    
# 이렇게 다 돌리고 나면 result라는 리스트에 정수들이 들어있겠지?
# 그러면 이 리스트 안에 있는 정수를 다 더해야 한다
length = len(result)
sum = 0

for i in range(length):
    sum += result[i]
print(sum)