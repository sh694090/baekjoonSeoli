from sys import stdin as s

# 알파벳으로 구성된 문자, 정수 입력
# 문자열에서 정수에 해당하는 위치의 문자 제거하고 출력
# 문자 1개가 남으면 종료하는 프로그램
# 주어진 정수가 문자열의 길이 이상인 경우 마지막 문자 제거
# 위치는 0부터 주어짐

word = list(s.readline().strip())

while len(word) >= 1:
    line = s.readline()
    if not line:
        break

    num = int(line.strip())
    if len(word) >= num:
        word.pop(num)
    elif len(word) < num:
        word.pop(-1)
    result = ''.join(word)
    print(result)