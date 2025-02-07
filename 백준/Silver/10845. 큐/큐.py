from sys import stdin as s

# 주어지는 명령의 수
N = int(s.readline().rstrip())

# 정수를 저장하는 큐
num_queue = []

def push(num):
    global num_queue
    num_queue += [num]

# 가장 앞에 있는 정수를 빼고, 그 수 출력함
# 큐에 정수 없는 경우 -1 출력
def pop():
    if len(num_queue) > 0:
        print(num_queue[0])
        num_queue.pop(0)
    else:
        print(-1)

def size():
    print(len(num_queue))

def empty():
    if len(num_queue) == 0:
        print(1)
    else:
        print(0)

def front():
    if len(num_queue) > 0:
        print(num_queue[0])
    else:
        print(-1)

def back():
    if len(num_queue) > 0:
        print(num_queue[-1])
    else:
        print(-1)

for _ in range(N):
# 주어지는 명령 (N번 반복)
    inp = s.readline().rstrip().split()
    
    if len(inp) > 1:
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
    elif command == 'front':
        front()
    else:
        back()