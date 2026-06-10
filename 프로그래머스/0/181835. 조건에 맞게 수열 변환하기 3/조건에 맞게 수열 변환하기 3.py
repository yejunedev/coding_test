def solution(arr, k):
    answer = []
    if (k%2==1):
        answer+=(x*k for x in arr)
    else:
        answer+=(x+k for x in arr)
    return answer