number_count = [0] * 10    # 0 ~ 9까지 숫자의 등장 횟수 저장하는 배열
N = input()    # 자연수 N을 입력받는다

# N의 모든 수를 순회하며 등장 횟수를 배열에 저장한다
for number in N:
    index = int(number)
    number_count[index] += 1
    
number_count[6] = ((number_count[6] + number_count[9]) + 1) // 2
number_count[9] = 0

result = max(number_count)
print(result)