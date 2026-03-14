def solution(strArr):
    answer = []
    n=len(strArr)
    for i in range(n):
        if i%2==1:
            answer.append(strArr[i].upper())
        else:
            answer.append(strArr[i].lower())
            
    return answer