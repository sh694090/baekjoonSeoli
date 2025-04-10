from sys import stdin as s

# 최대 100개의 세자리 이하의 정수 주어지다가
# 999 또는 -999가 주어지면 입력받는 것 종료
# 이 수 제외한 가장 큰 수, 가장 작은 수 출력

# 우선 주어진 수 다 입력 받음
arr = list(map(int, s.readline().split()))

# 새로운 리스트 만들어서 주어진 수를 하나씩 새로운 리스트에 넣음
# 하나씩 순회하다가 999나 -999 나오면 그대로 반복문 종료
new_arr = []
for elem in arr:
    if elem == 999 or elem == -999:
        break
    else:
        new_arr.append(elem)

min_val = min(new_arr)
max_val = max(new_arr)

print(max_val, min_val)