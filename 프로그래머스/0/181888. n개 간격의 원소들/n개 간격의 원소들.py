def solution(num_list, n):
    answer = []
    a = len(num_list)
    for i in range(a):
        answer+=num_list[:a:+n]
        break
    return answer