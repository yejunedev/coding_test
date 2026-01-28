def solution(a, b):
    a = str(a)
    b = str(b)
    x = a+b
    y = b+a
    x = int(x)
    y = int(y)
    answer = max(x,y)
    return answer