def solution(arr1, arr2):
    answer = 0
    a=len(arr1)
    b=len(arr2)
    
    if a<b:
        answer = -1
    elif a>b:
        answer =  1
    elif a==b:
        sum1 = sum(arr1)
        sum2 = sum(arr2)
        if sum1>sum2:
            answer = 1
        elif sum1<sum2:
            answer = -1
        elif sum1==sum2:
            answer = 0
    return answer