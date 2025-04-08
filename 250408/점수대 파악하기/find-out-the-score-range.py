from sys import stdin as s

# 100명 이하인 학생들의 점수가 주어짐
# 0이 주어지면 그 전까지의 점수를 10의 자리만 뽑아서
# 점수대별 학생 수 출력

arr = list(map(int, s.readline().split()))

# 0 이전 입력값의 10의 자리 수 new_arr에 추가
new_arr = []
for elem in arr:
    if elem == 0:
        break
    else:
        new_arr.append(elem // 10)

# 해당 10의 자리 수를 같은 인덱스에 개수 추가
# 해당 개수를 cnt_arr에 저장
# cnt_arr의 인덱스가 1일 때 new_arr[i]가 1이라면 cnt_arr에 +1
cnt_arr = [0] * 11
for elem in new_arr:
    cnt_arr[elem] += 1

for i in range(10, 0, -1):
    cnt = cnt_arr[i]
    print(f"{i * 10} - {cnt}")