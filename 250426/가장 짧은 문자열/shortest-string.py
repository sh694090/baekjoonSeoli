from sys import stdin as s

str1 = s.readline().rstrip()
str2 = s.readline().rstrip()
str3 = s.readline().rstrip()

len1 = len(str1)
len2 = len(str2)
len3 = len(str3)

result = max(len1, len2, len3) - min(len1, len2, len3)

print(result)