def solution(code):
    answer = ''
    mode = 0
    for i in range(len(code)):
        c = code[i]
        if c=='1':
            if mode==0:
                mode = 1
            else:
                mode = 0
        else:
            if mode==0:
                if i%2==0:
                    answer+=c
            else:
                if i%2==1:
                    answer+=c
                    
    if answer=='':
        answer = 'EMPTY'
            
    return answer