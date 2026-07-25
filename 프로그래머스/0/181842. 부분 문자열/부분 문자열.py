def solution(str1, str2):
    answer = 0
    set(str2)
    if str1 in str2:
        return 1
    elif str1 not in str2:
        return 0
    return answer