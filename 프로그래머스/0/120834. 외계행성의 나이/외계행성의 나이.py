def num2ch(x):
    if x=='0':
        return 'a'
    elif x=='1':
        return 'b'
    elif x=='2':
        return 'c'
    elif x=='3':
        return 'd'
    elif x=='4':
        return 'e'
    elif x=='5':
        return 'f'
    elif x=='6':
        return 'g'
    elif x=='7':
        return 'h'
    elif x=='8':
        return 'i'
    elif x=='9':
        return 'j'

def solution(age):
    arr = str(age)
    arr = list(arr)
    answer = ''
    for a in arr:
        answer+=num2ch(a)
    return answer