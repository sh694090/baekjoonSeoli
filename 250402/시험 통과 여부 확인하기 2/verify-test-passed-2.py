from sys import stdin as s

# 10명 미만의 학생 => 시험 4개 봐서 점수 얻음
# 4개 시험의 평균 점수가 60점 이상 => 통과
# 평균 점수가 통과인 경우 pass 출력
# 통과 아닌 경우 fail 출력

# 최종적으로 통과한 학생의 수 출력

# 주어지는 학생 수는 크게 중요하진 않고 몇 줄에 걸쳐서 문항이 나오는지 확인하는거네

N = int(s.readline().rstrip())

cnt = 0
for i in range(N):
    grade = list(map(int, s.readline().split()))
    grade_sum = sum(grade)
    grade_avg = grade_sum / 4

    if grade_avg >= 60:
        cnt += 1
        print("pass")
    else:
        print("fail")
print(cnt)
