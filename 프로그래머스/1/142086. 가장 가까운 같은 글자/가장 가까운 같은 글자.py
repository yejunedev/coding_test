def solution(s):
    answer = []
    cnt=0
    mydic = dict()
    n = len(s)
    for i in range(n):
        if s[i] not in mydic:
            answer.append(-1)
            mydic[s[i]] = [i]
        else:
            answer.append(i - mydic[s[i]][-1])
        mydic[s[i]].append(i)
                        
    return answer