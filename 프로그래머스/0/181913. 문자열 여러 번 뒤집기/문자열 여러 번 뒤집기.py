def solution(my_string, queries):
    answer = ''
    for [s,e] in queries:
        ts = ''
        ts += my_string[0:s]
        for i in range(e, s-1, -1):
            ts += my_string[i]
        ts += my_string[e+1:]
        my_string = ts[:]
    answer = my_string[:]
    return my_string