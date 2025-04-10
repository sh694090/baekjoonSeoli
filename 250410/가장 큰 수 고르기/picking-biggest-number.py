from sys import stdin as s

# 정수 10개가 주어지면 그 중 가장 큰 수 골라 출력
arr = list(map(int, s.readline().split()))

print(max(arr))