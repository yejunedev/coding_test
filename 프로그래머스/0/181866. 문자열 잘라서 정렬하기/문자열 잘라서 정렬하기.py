def solution(myString):
    answer = []
    for t in myString.split('x'):
        if t!='':
            answer.append(t)
    answer.sort()
    return answer