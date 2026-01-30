def solution(a, b, c):
    answer = 0
    if a != b != c and b != c != a and c != a != b:
        answer = a + b + c
    elif a == b != c or a == c != b or  b == c != a:
        answer = (a + b + c)*(a*a + b*b + c*c)
    elif a == b == c:
        answer = (a + b + c)*(a*a + b*b + c*c)*(a*a*a + b*b*b + c*c*c)
    return answer