from sys import stdin as s

arr = ['apple', 'banana', 'grape', 'blueberry', 'orange']

alp = s.readline().strip()

cnt = 0
# 3번째나 4번째에 alp가 있으면 문자열 앤나 개수 출력
for elem in arr:
    if elem[2] == alp or elem[3] == alp:
        print(elem)
        cnt += 1

print(cnt)