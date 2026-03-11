def solution(arr):
    answer = 0
    for a in arr:
        x=a # 이전값
        y=a # 현재값
        cnt=0
        while True:
            if y>=50 and y%2==0:
                y=y//2
            elif y<50 and y%2==1:
                y=2*y+1
            if x==y:
                break
            cnt+=1
            x=y
        
        answer = max(answer,cnt)
                    
    return answer