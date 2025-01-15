# 정수 a, b를 공백을 사이에 두고 입력한다
inp = input().split()

a = int(inp[0])
b = int(inp[1])

# a / b의 정수값 먼저 출력한다
print(f"{a // b}.", end = "")

# a / b의 나머지 * 10을 b로 나눈 몫을 20번 출력한다
for i in range(20):
    a *= 10
    print(a // b, end = "")
    a %= b