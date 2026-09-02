def solution(s):
    answer = True
    l=len(s)
    if l==4 and l==6 and s.isdigit():
        return answer
    elif l!=4 and l!=6 or not s.isdigit():
        return False
    return answer