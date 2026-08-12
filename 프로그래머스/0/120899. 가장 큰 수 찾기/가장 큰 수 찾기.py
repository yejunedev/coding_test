def solution(array):
    mx=-1
    idx=-1
    n=len(array)
    for i in range(n):
        if mx < array[i]:
            mx=array[i]
            idx=i
    return [mx, idx]