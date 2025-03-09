from sys import stdin as s

cnt = 0
total = 0
while True:
    age = int(s.readline().rstrip())

    if age >= 30:
        print(f"{avg:.2f}")
        break

    cnt += 1
    total += age
    avg = total / cnt