# 010-xxxx-yyyy 형태로 전화번호를 입력한다
number = input().split("-")

front = int(number[1])
back = int(number[2])

# 입력받은 번호의 앞자리와 뒷자리를 바꾼다
front, back = back, front

# 입력받은 번호의 앞자리와 뒷자리의 위치가 바뀐 형태를 출력한다
print(f"010-{front}-{back}")