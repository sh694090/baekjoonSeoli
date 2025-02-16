from sys import stdin as s
from collections import deque

while True:

    inp = s.readline().rstrip()
    inp_list = list(inp.strip())

    # inp_list = list(s.readline().strip())

    if inp == '.':
        break

    N = len(inp_list)

    stk = []

    for i in range(N):
        # 문자가 '(' 또는 '['인 경우 스택에 추가
        if inp_list[i] == '(' or inp_list[i] == '[':
            stk.append(inp_list[i])
        # 문자가 ')'인 경우 스택 마지막 인덱스에 '(' 있는지 확인
        elif inp_list[i] == ')':
        # 스택에 '(' 있으면 삭제
            if len(stk) >= 1 and stk[-1] == '(':
                stk.pop()
        # 없으면 쌍이 안맞으므로 no 출력
            else:
                print('no')
                break
        # 문자가 ']'인 경우 스택 마지막 인덱스에 '[' 있는지 확인
        elif inp_list[i] == ']':
        # 스택에 '[' 있으면 삭제
            if len(stk) >= 1 and stk[-1] == '[':
                stk.pop()
        # 없으면 쌍이 안맞으므로 no 출력
            else:
                print('no')
                break
    # no 조건이 하나도 해당하지 않는다면 yes 출력
    else:
        print('yes' if not stk else 'no')