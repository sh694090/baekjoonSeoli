from sys import stdin as s

inp = s.readline().strip()

cnt_ee = 0
cnt_eb = 0

# 각각 몇번 나왔는지 출력
# inp에서 e로 시작해서 e로 끝나는 문자열이 있었는지 확인하고 해당 개수가 몇 개 있었는지 확인
# ee, eb가 주어진 문자열에 없는 경우도 있을 것 같은데

if 'ee' in inp:
    for i in range(len(inp) - 1):
        if inp[i] == 'e' and inp[i + 1] == 'e':
            cnt_ee += 1

if 'eb' in inp:
    for i in range(len(inp) - 1):
        if inp[i] == 'e' and inp[i + 1] == 'b':
            cnt_eb += 1

print(cnt_ee, cnt_eb)