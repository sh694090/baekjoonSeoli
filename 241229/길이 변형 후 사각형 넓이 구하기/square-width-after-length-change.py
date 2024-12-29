# 정수형인 가로 길이, 세로 길이를 입력한다
length = input().split()

width = int(length[0])
height = int(length[1])

# 가로 길이 + 8, 세로 길이 * 3를 저장한다
width += 8
height *= 3

# 가로 길이, 세로 길이, 넓이를 각 줄에 출력한다
print(width)
print(height)
print(width * height)