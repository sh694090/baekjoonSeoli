# 정수 n을 입력한다
n = int(input())

# 정수 n >= 80인 경우 pass 출력
if n >= 80:
    print('pass')
# 정수 n < 80인 경우 "(80 - n) more score"의 결과 출력
if n < 80:
    print(f"{80 - n} more score")