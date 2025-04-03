from sys import stdin as s

# 문자 10개 입력받아서 2, 5, 8번째 문자 차례대로 출력

arr = list(map(str, s.readline().split()))

print(arr[1], arr[4],arr[7])
