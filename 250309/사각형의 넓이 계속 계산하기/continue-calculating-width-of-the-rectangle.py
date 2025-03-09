from sys import stdin as s

# string에 C가 나오면 멈춰
while True:
    inp = s.readline().rstrip().split()

    width = int(inp[0])
    height = int(inp[1])
    string = inp[2]

    area = width * height
    print(area)
    
    if string == 'C':
        break