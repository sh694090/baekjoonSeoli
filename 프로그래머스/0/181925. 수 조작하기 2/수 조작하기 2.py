def solution(numLog):
    answer = ''
    n = numLog[0]
    for i in range(1, len(numLog)):
        if numLog[i] - numLog[i -1] == 1:
            answer += 'w'
        elif numLog[i] - numLog[i -1] == -1:
            answer += 's'
        elif numLog[i] - numLog[i -1] == 10:
            answer += 'd'
        else:
            answer += 'a'
    return answer