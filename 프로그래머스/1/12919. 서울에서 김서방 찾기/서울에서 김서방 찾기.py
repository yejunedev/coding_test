def solution(seoul):
    answer = 0
    for i in seoul:
        if i=='Kim':
            break
        answer+=1
    return f'김서방은 {answer}에 있다'