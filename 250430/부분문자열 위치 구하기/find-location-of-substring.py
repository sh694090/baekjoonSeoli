from sys import stdin as s

input_str = s.readline().strip()
target_str = s.readline().strip()

result = input_str.find(target_str)
print(result)