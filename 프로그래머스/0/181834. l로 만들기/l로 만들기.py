def solution(myString):
    answer = ''
    for s in myString:
        # 아스키코드로 비교
        # ord(s)
        if ord(s) < ord('l'):
            answer += 'l'
        else:
            answer += s
            
            
    return answer