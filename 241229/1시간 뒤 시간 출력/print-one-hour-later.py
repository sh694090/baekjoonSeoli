# h:m 형태로 시간과 분을 입력한다
time = input().split(":")
h = int(time[0])
m = int(time[1])

# h + 1:m 형태로 시간과 분을 출력한다
print(f"{h + 1}:{m}")