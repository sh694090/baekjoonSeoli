from sys import stdin as s

# 감기 증상 있으면 "Y"
# 증상 없으면 "N"

# 증상 있고 + 37 이상일 때 A
# 증상 없고 + 37 이상일 때 B
# 증상 있고 + 37 미만 C
# 둘 다 괜찮은 경우 D

med_arr = [0] * 5
# A로 가면 index 1
# B로 가면 index 2
# C로 가면 index 3
# D로 가면 index 4

# 한 줄에 한명씩 감기 증상, 체온 공백을 사이에 두고 입력 (3명)

# A, B, C, D 진료소로 보내지는 인원 순서대로 출력
# A로 가는 사람이 2명 이상인 경우 마지막에 E 출력

for i in range(3):
    patient_arr = list(map(str, s.readline().split()))
    if patient_arr[0] == "Y":
        if int(patient_arr[1]) >= 37:
            med_arr[1] += 1
        else:
            med_arr[3] += 1
    elif patient_arr[0] == "N":
        if int(patient_arr[1]) >= 37:
            med_arr[2] += 1
        else:
            med_arr[4] += 1

for i in range(1, 5):
    print(med_arr[i], end = " ")

if med_arr[1] >= 2:
    print("E")
