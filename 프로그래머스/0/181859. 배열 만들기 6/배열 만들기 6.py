def solution(arr):
    stk = []
    for a in arr:
        if stk==[]:
            stk.append(a)
        else:
            if stk[-1]==a:
                stk.pop()
            else:
                stk.append(a)
    if stk==[]: stk.append(-1)        
    return stk