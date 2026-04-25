def solution(arr, flag):
    answer = []
    n = len(arr)
    for i in range(n):
        if flag[i]==True:
            for j in range(arr[i]*2):
                answer.append(arr[i])
        else:
            for j in range(arr[i]):
                answer.pop()
        
        
        
    
    
    return answer