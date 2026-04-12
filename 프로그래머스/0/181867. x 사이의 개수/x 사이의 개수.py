def solution(myString):
    answer = []
    parts=myString.split('x')
    for i in parts:
        answer.append(len(i))
        
    return answer