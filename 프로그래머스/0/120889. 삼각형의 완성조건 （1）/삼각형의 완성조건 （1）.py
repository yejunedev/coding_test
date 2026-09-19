def solution(sides):
    sides.sort()
    a=sides[0]+sides[1]
    b=sides[2]
    if a>b:
        return 1
    else:
        return 2
    