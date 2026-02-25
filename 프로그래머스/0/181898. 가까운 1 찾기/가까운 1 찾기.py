def solution(arr, idx):
    n=len(arr)
    answer = -1
    for i in range(idx,n):
        
        if arr[i]==1:
            answer = i
            break
    return answer