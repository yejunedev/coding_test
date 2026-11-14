def solution(num_list, n):
    answer = []
    # 0 +=2 -> 2
    # i + n [i:i+n]
    
    for i in range(0,len(num_list),n):
        answer.append(num_list[i:n+i])
    
    return answer
