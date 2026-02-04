def solution(num_list):
    #누적합
    s = 0
    # 누적곱
    p = 1
    for x in num_list:
        s = s+x
        p = p*x
        
    s = s*s
    if p<s:
        answer = 1
    else:
        answer = 0
    return answer