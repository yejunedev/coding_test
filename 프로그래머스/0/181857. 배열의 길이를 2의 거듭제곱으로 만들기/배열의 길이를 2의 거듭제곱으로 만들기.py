def solution(arr):
    answer = arr[:]
    n=len(arr)
    m = 1
    while m<n:
        m = 2*m
    for i in range(m-n):
        answer.append(0)
    return answer