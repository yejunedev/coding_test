def solution(emergency):
    arr=emergency[:]
    arr.sort(reverse=True)
    n = len(arr)
    answer=[]
    for e in emergency:
        for i in range(n):
            if e==arr[i]:
                answer.append(i+1)
                break
    return answer