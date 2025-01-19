N = int(input())
int_list = input().split()
v = int(input())

# -100 <= v <= 100이므로
v_size = 201

# 등장한 정수의 개수를 저장하는 배열 생성
int_count = [0] * v_size

for i in range (0, N):
    index = int(int_list[i]) + 100
    int_count[index] += 1

result = int_count[v + 100]
print(result)