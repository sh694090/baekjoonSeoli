from sys import stdin as s

word = list(s.readline().strip())

while len(word) >= 1:
    inp = s.readline()

    if not inp:
        break
    
    num = int(inp.strip())
    if len(word) > num:
        word.pop(num)
    else:
        word.pop(-1)
    result = ''.join(word)
    print(result)

    