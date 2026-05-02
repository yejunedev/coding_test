import random

def solution(arr, k):
    answer = []
    for a in arr:
        if a in answer:
            continue
        answer.append(a)
        
    if len(answer)>=k:
        answer = answer[:k]
    else:
        m = len(answer)
        for i in range(k-m):
            answer.append(-1)
    return answer