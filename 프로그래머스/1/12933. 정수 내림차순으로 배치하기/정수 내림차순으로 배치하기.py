def solution(n):
    A = list(str(n))
    A.sort()
    A.reverse()
    answer = ''.join(A)
    return int(answer)