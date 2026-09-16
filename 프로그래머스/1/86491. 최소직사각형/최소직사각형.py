def solution(sizes):
    hmax, vmax = 0, 0
    for size in sizes:
        h = max(size)
        v = min(size)
        hmax=max(hmax, h)
        vmax=max(vmax, v)
        
    answer=hmax*vmax
    return answer