def solution(number):
    s=0
    for x in number:
        s+=int(x)
    answer = s%9
    return answer