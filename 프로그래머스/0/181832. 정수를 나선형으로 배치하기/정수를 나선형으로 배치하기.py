def solution(n):
    arr = [
        [0 for c in range(n)]
        for r in range(n)
    ]
    
    r,c=0,-1
    dir=1
    ln=n
    num=1
    
    while True:
        # -- 가로 방향
        for i in range(ln):
            c=c+dir
            arr[r][c] = num
            num+=1
        
        # 길이 감소
        ln -= 1
        # 길이가 0이면 종료
        if ln==0:
            break
                
        # | 세로 방향
        for i in range(ln):
            r=r+dir
            arr[r][c]= num
            num+=1
        
        # 방향전환
        dir = -dir
        
    return arr