# 첫 번째 줄에 정수 a, b를 공백을 사이에 두고 입력한다
inp = input().split()

a = int(inp[0])
b = int(inp[1])

# a부터 b까지의 수 중 5 또는 7의 배수의 합, 평균 출력
# 평균은 반올림해서 소수점 첫째자리까지 출력
sum_val = 0
average_val = 0
cnt = 0

for i in range(a, b + 1):
    if i % 5 == 0 or i % 7 == 0:
        sum_val += i
        cnt += 1
average_val = sum_val / cnt
print(sum_val, f"{average_val:.1f}")