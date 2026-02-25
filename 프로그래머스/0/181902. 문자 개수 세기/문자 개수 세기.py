def solution(my_string):
    answer = [0]*52
    for s in my_string:
        if s.isupper():
            x=ord(s)-65
            answer[x]+=1
        else:
            x=ord(s)-97+26
            answer[x]+=1
    
    return answer
