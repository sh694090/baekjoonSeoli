from sys import stdin as s

A, B = s.readline().split()

AB = str(A) + str(B)
BA = str(B) + str(A)

result = int(AB) + int(BA)
print(result)