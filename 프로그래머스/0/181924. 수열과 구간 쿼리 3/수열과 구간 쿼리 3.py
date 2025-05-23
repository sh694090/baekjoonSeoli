def solution(arr, queries):
    for elem in queries:
        i = elem[0]
        j = elem[1]
        arr[i], arr[j] = arr[j], arr[i]
    return arr