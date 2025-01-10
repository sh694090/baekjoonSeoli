# 첫 번째 사람의 나이, 성별을 공백을 두고 작성한다
first = input().split()

first_age = int(first[0])
first_sex = first[1]

# 두 번째 사람의 나이, 성별을 공백을 두고 작성한다
second = input().split()

second_age = int(second[0])
second_sex = second[1]

# 두 사람 중 한 명이라도 19세 이상 and M이면 1 출력, 아니면 0 출력
if (first_age >= 19 and first_sex == 'M') or (second_age >= 19 and second_sex == 'M'):
    print(1)
else:
    print(0)