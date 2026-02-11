def solution(a, b, c, d):
    answer = 0
    if a==b==c==d:
        answer = 1111*a
    elif a==b==c:
        answer = (10*a+d)**2
    elif b==c==d:
        answer = (10*b+a)**2
    elif c==d==a:
        answer = (10*c+b)**2
    elif d==a==b:
        answer = (10*d+c)**2
    elif a==b:
        if c==d:
            answer = (a+c)*abs(a-c)
        else:
            answer = c*d
    elif a==c:
        if b==d:
            answer = (a+b)*abs(a-b)
        else:
            answer = b*d
    elif a==d:
        if b==c:
            answer = (a+b)*abs(a-b)
        else:
            answer = b*c
    elif b==c:
        if d==a:
            answer = (b+d)*abs(b-d)
        else:
            answer = d*a
    elif b==d:
        if c==a:
            answer = (b+c)*abs(b-c)
        else:
            answer = c*a
    elif c==d:
        if a==b:
            answer = (c+a)*abs(c-a)
        else:
            answer = a*b
    else:
        answer = min(a,b,c,d)
            
    return answer