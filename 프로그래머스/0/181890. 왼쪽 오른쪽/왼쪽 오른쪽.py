def solution(str_list):
    answer = []
    n = len(str_list)
    for i in range(n):
        if str_list[i]=="l":
            answer = str_list[:i]
            break
        if str_list[i]=="r":
            answer = str_list[i+1:]
            break
    return answer