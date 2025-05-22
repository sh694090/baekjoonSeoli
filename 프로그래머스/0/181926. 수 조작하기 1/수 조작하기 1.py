def solution(n, control):
    for elem in control:
        if elem == 'w':
            n += 1
        elif elem == 's':
            n -= 1
        elif elem == 'd':
            n += 10
        else:
            n -= 10
    return n