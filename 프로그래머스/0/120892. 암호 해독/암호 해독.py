def solution(cipher, code):
    n=len(cipher)
    answer = ''
    for i in range(code-1,n,code):
        answer+=cipher[i]
    return answer