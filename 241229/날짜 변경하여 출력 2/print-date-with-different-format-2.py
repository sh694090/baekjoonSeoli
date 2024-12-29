# 날짜를 mm-dd-yyyy 형태로 입력한다
date = input().split("-")

month = int(date[0])
day = int(date[1])
year = int(date[2])

# 입력 받은 날짜를 yyyy.mm.dd 형태로 출력한다
print(f"{year}.{month}.{day}")