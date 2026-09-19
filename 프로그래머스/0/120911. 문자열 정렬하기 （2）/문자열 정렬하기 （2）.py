def solution(my_string):
    arr = []
    for s in my_string:
        if s.isupper():
            arr.append(s.lower())
        else:
            arr.append(s)
    arr.sort()
    return ''.join(arr)