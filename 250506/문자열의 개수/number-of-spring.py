from sys import stdin as s

# 알파벳으로 구성된 문자열 연속 입력
# 문자열 대신 0 입력되면 입력 종료
# 그 전까지 입력된 문자열의 총 개수 출력
# 입력된 문자열 중 홀수번째에 해당하는 문자열 순서대로 한 줄에 하나씩 출력

arr = []
while True:
    inp = s.readline().strip()
    if inp == '0':
        break
    else:
        arr.append(inp)

cnt = len(arr)
print(cnt)

for i in range(len(arr)):
    if (i) % 2 == 0:
        print(arr[i])
    else:
        continue

