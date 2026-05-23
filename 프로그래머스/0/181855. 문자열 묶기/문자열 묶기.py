def solution(strArr):
    arr = [[] for i in range(31)]
    for a in strArr:
        n = len(a)
        # 길이에 따라 삽입
        arr[n].append(a)
        
    answer = 0
    for i in range(1, 31):
        if len(arr[i])==0:
            continue
        n = len(arr[i])
        answer = max(answer, n)
    
    return answer