from sys import stdin as s
string = list(s.readline().rstrip())
left = string
right = []

m = int(s.readline().rstrip())

for i in range (m):
    command = s.readline().rstrip().split()
    if command[0] == 'L':
        if left:
            right.append(left.pop())
    elif command[0] == 'D':
        if right:
            left.append(right.pop())
    elif command[0] == 'B':
        if left:
            left.pop()
    elif command[0] == 'P':
        char = command[1]
        left.append(char)
right.reverse()
result = ''.join(left + right)
print(result)