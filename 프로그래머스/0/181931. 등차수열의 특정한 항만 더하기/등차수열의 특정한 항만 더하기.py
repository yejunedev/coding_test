def solution(a, d, included):
    answer = 0
    for x in included:
        if x==True:
            answer+=a
        a+=d
    return answer