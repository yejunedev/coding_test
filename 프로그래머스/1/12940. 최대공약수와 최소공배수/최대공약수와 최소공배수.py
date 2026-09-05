def solution(n, m):
    a = n
    b = m
    while b!=0:
        a,b=b,a%b
        
    answer = [a,(n*m)//a]
    
    return answer