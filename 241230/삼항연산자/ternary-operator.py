# 시험 점수를 입력받는다
# 근데 시험 점수가 정수인지 실수인지 모르겠다. 숫자니까 그냥 정수라고 해보자
score = int(input())

result = 'pass' if score == 100 else 'failure'
print(result)