import re

def solution(myStr):
    arr = re.split("[abc]",myStr)
    answer = []
    for a in arr:
        if len(a)==0:
            continue
        answer.append(a)
    if len(answer)==0:
        answer = ["EMPTY"]
    return answer