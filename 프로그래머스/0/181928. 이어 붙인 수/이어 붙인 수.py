def solution(num_list):
    a = ''
    b = ''
    for x in num_list:
        if x%2==0:
            a = a + str(x)
        else:
            b = b+str(x)
    # 문자열화된 숫자 a, b를 정수로
    a = int(a)
    b = int(b)
    answer = a+b        
    return answer