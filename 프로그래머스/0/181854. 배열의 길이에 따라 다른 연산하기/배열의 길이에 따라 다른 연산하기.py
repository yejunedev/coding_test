def solution(arr, n):
    x=len(arr)
    if(x%2==1):
        for i in range(0,x,2):
            arr[i]+=n
    else:
        for i in range(1,x,2):
            arr[i]+=n  
    return arr