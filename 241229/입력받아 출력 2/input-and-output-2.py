# 앞자리 6자리, 뒷자리 7자리로 구성된 주민번호를 입력한다
reg_number = input().split("-")

front = int(reg_number[0])
back = int(reg_number[1])

# 입력받은 값에서 -를 제외한 결과를 출력한다
print(f"{front}{back}")