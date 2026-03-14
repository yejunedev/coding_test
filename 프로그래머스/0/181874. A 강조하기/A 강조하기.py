def solution(myString):
    answer = ''
    for i in myString:
        if i=='a':
            answer += i.upper()
        elif i!='A':
            if i.isalpha() and i.isupper():
                answer += i.lower()
            else:
                 answer += i
        else:
            answer+=i
            
            
    return answer