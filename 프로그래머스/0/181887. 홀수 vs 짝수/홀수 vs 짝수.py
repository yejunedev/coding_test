def solution(num_list):
    answer = 0
    a=sum(num_list[0::2])
    b=sum(num_list[1::2])
    answer = max(a,b)
    return answer

