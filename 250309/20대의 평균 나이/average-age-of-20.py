from sys import stdin as s

total = 0
cnt = 0

while True:
# 나이를 입력받는다
    age = int(s.readline().rstrip())

# 입력받는 나이가 20대인지 확인 후 20대가 아니면 break
    if age < 20 or age >= 30:
        break

# 20대이면 total에 더함
    total += age
    cnt += 1

    avg = total / cnt

print(f"{avg:.2f}")