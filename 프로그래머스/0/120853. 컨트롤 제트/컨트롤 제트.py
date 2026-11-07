def solution(s):
    answer = 0
    arr = s.split()
    stk = []
    for a in arr:
        if a=="Z":
            if len(stk)>0:
                stk.pop()
        else:
            stk.append(int(a))
            
    answer = sum(stk)      
    return answer