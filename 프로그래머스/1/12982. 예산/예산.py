def solution(d, budget):
    d.sort()
    answer = 0
    tot = 0
    for i in d:
        tot+=i
        if tot <= budget:
            answer+=1
    return answer