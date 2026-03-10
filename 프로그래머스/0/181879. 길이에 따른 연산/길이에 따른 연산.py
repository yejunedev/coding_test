def solution(num_list):
    answer = 0
    n=len(num_list)
    if n>=11:
        for i in num_list:
            answer+=i
    else:
        answer = 1
        for i in num_list:
            answer*=i
            
    return answer