def solution(my_string, is_suffix):
    answer = 0
    n=len(my_string)
    arr=[]
    for i in range(n):
        arr.append(my_string[i:])
        
        if is_suffix in arr:
            answer = 1
        else:
            answer = 0
            
    return answer