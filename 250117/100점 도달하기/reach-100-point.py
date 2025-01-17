# 점수 n을 입력한다
n = int(input())
# n부터 100까지 순회하면서 해당 점수에 해당하는 등급을 공백을 사이에 두고 한 줄로 출력
for i in range(n, 101):
    if i >= 90:
        print("A", end = " ")
    elif i >= 80:
        print("B", end = " ")
    elif i >= 70:
        print("C", end = " ")
    elif i >= 60:
        print("D", end = " ")
    else:
        print("F", end = " ")