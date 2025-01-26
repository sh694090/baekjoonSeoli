from sys import stdin as s

# for문을 돌리는 횟수
num = int(s.readline().rstrip())

for _ in range(num):

    # 강산이가 입력한 값 입력 받음
    inp = list(s.readline().rstrip())
    length = len(inp)

    cursor_left = []
    cursor_right = []
    
    for i in range(length):
        
        if inp[i] == "<":
            if cursor_left:
                cursor_right.append(cursor_left.pop())
        elif inp[i] == ">":
            if cursor_right:
                cursor_left.append(cursor_right.pop())
        elif inp[i] == "-":
            if cursor_left:
                cursor_left.pop()
        else:
            cursor_left.append(inp[i])
    cursor_right.reverse()
    password = ''.join(cursor_left + cursor_right)
    print(password)