from sys import stdin as s

A = s.readline().strip()
B = s.readline().strip()

str1 = A + B
str2 = B + A

if str1 == str2:
    print("true")
else:
    print("false")