def solution(numbers):
    answer = -100000000
    n = len(numbers)
    for i in range(n):
        for j in range(n):
            if i==j: continue
            a = numbers[i]
            b = numbers[j]
            if answer < a*b:
                answer = a*b
    return answer