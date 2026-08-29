def get(x):
    cnt=2
    if x==1: cnt = 1
    i=2
    while i*i<=x:
        if x%i==0:
            j=x//i
            if i==j: cnt+=1
            else: cnt+=2
        i+=1
        
    return cnt

def solution(left, right):
    answer = 0
    for i in range(left,right+1):
        cnt = get(i)
        if cnt%2==0:
            answer+=i
        else:
            answer-=i
                       
    return answer