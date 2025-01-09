# 중간, 기말 점수를 공백에 사이에 두고 입력한다
mid, final = input().split()

mid = int(mid)
final = int(final)

# 중간 >= 90 and 기말 >= 95이면 100000
if mid >= 90 and final >= 95:
    print(100000)

# 중간 >= 90 and 기말 > 90이면 50000
elif mid >= 90 and final >= 90:
    print(50000)

# 이외는 0
else:
    print(0)