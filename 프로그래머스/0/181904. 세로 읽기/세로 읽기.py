def solution(my_string, m, c):
    n = len(my_string)
    answer = ''
    for i in range(c-1,n,m):
        answer+=my_string[i]
    return answer