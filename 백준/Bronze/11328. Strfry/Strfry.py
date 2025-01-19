N = int(input())

for i in range (N):
    inp = input().split()

    str1 = inp[0]
    str2 = inp[1]

    alphabet_count1 = [0] * 26
    alphabet_count2 = [0] * 26

    for char in str1:
        index = ord(char) - ord('a')
        alphabet_count1[index] += 1

    for char in str2:
        index = ord(char) - ord('a')
        alphabet_count2[index] += 1

    if alphabet_count1 == alphabet_count2:
        print("Possible")
    else:
        print("Impossible")