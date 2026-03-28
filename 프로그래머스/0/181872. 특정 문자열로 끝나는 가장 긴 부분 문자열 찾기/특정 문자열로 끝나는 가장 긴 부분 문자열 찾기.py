def solution(myString, pat):
    answer = ''
    n=len(myString)
    for i in range(n):
        answer+=myString[i]
        if answer.endswith(pat):
            result = answer
    return result