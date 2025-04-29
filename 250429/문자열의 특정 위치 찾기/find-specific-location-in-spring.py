from sys import stdin as s

inp = list(s.readline().split())

word = inp[0]
alp = inp[1]

if alp in word:
    print(word.index(alp))
else:
    print("No")