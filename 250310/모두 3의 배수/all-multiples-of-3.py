from sys import stdin as s

is_multiple = True

for _ in range(5):
    inp = int(s.readline().rstrip())
    
    if inp % 3 != 0:
        is_multiple = False

if is_multiple == True:
    print(1)
else:
    print(0)