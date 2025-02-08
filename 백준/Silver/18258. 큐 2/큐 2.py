# push X
# 정수 X를 큐에 넣는 연산

from collections import deque
from sys import stdin as s

# 주어지는 명령의 수
N = int(s.readline().rstrip())

dq = deque()

def push(X):
    dq.append(X)

def pop():
    if dq:
        print(dq.popleft())
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

    if command[0] == 'push':
       X = command[1]
       push(X)
    elif command[0] == 'pop':
       pop()
    elif command[0] == 'size':
       size()
    elif command[0] == 'empty':
       empty()
    elif command[0] == 'front':
       front()
    else:
       back()