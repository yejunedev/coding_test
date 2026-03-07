def solution(names):
    answer = []
    n = len(names)
    for i in range(0,n,5):
        answer.append(names[i])
    return answer