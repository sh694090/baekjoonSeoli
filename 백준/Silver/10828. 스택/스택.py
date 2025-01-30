from sys import stdin as s
N = int(s.readline().rstrip())

result = []

def push(num):
    result.append(num)

def pop():
    if len(result) > 0:
        print(result.pop())
    else:
        print(-1)

def size():
    print(len(result))

def empty():
    if len(result) == 0:
        print(1)
    else:
        print(0)

def top():
    if len(result) > 0:
        print(result[len(result) - 1])
    else:
        print(-1)

for _ in range (N):
    inp = s.readline().rstrip().split()

    if len(inp) >= 2:
        command = inp[0]
        num = int(inp[1])
    else:
        command = inp[0]

    if command == 'push':
        push(num)
    elif command == 'pop':
        pop()
    elif command == 'size':
        size()
    elif command == 'empty':
        empty()
    elif command == 'top':
        top()