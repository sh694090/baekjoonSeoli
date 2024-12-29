# yyyy.mm.dd 형태로 날짜를 입력한다
date = input().split(".")

year = int(date[0])
month = int(date[1])
day = int(date[2])

# 입력받은 날짜를 mm-dd-yyyy 형식으로 출력한다
print(f"{month}-{day}-{year}")