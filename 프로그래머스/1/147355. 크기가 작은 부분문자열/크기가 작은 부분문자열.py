def solution(t, p):
    answer = 0
    n=len(t)
    m=len(p)
    b=int(p)
    for i in range(n-m+1):
        s=t[i:i+m]
        a=int(s)
        if a<=b:
            answer+=1
    return answer