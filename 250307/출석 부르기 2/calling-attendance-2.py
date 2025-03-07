from sys import stdin as s

while True:
    inp = int(s.readline().rstrip())
    if inp == 1:
        print('John')
    elif inp == 2:
        print('Tom')
    elif inp == 3:
        print('Paul')
    elif inp == 4:
        print('Sam')
    else:
        print('Vacancy')
        break