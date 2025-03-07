from sys import stdin as s

while True:
    inp = int(s.readline().rstrip())

    if inp < 25:
        print('Higher')
    elif inp > 25:
        print('Lower')
    else:
        print('Good')
        break