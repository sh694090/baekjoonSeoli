from sys import stdin as s

n = int(s.readline().strip())

result = ""
for _ in range(n):
    inp = s.readline().strip()
    result += inp

print(result)