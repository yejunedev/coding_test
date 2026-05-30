def solution(rank, attendance):
    n=len(rank)
    arr=[]
    
    for i in range(n):
        if attendance[i]==False:
            continue
        arr.append((rank[i], i))
    arr.sort()
    answer = arr[0][1]*10000+arr[1][1]*100+arr[2][1]
                
    return answer