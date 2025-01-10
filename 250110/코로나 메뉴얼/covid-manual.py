# 한 줄씩 3명의 감기 증상, 체온을 공백을 사이에 두고 입력한다.
inp = input().split()
cold1, temp1 = inp[0], int(inp[1])
inp = input().split()
cold2, temp2 = inp[0], int(inp[1])
inp = input().split()
cold3, temp3 = inp[0], int(inp[1])

# 첫 번째 사람이 A인 경우
if cold1 == 'Y' and temp1 >= 37:
    # 두 번째나 세 번째 사람 둘 중 하나가 A이면 E, 아니면 N
    if (cold2 == 'Y' and temp2 >= 37) or (cold3 == 'Y' and temp3 >= 37):
        print('E')
    else:
        print('N')
# 첫 번째 사람이 A가 아닌 경우
else:
    # 두 번째, 세 번째 사람 모두 A여야 E, 아니면 N
    if (cold2 == 'Y' and temp2 >= 37) and (cold3 == 'Y' and temp3 >= 37):
        print('E')
    else:
        print('N')