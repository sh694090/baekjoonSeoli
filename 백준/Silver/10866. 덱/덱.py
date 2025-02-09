from sys import stdin as s
from collections import deque

N = int(s.readline().rstrip())

dq = deque()

def push_front(X):
    dq.appendleft(X)

def push_back(X):
    dq.append(X)

def pop_front():
    if dq:
        print(dq.popleft())
    else:
        print(-1)

def pop_back():
    if dq:
        print(dq.pop())
    else:
        print(-1)

def size():
    print(len(dq))

def empty():
    if dq:
        print(0)
    else:
        print(1)

def front():
    if dq:
        print(dq[0])
    else:
        print(-1)

def back():
    if dq:
        print(dq[-1])
    else:
        print(-1)

for _ in range(N):
    command = list(s.readline().rstrip().split())

    if command[0] == 'push_front':
        X = command[1]
        push_front(X)
    elif command[0] == 'push_back':
        X = command[1]
        push_back(X)
    elif command[0] == 'pop_front':
        pop_front()
    elif command[0] == 'pop_back':
        pop_back()
    elif command[0] == 'size':
        size()
    elif command[0] == 'empty':
        empty()
    elif command[0] == 'front':
        front()
    else:
        back()