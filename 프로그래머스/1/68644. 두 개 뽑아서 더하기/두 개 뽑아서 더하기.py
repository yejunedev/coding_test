def solution(numbers):
    answer = []
    t=set()
    n = len(numbers)
    for i in range(n):
        for j in range(n):
            if i==j: continue
            num = numbers[i] + numbers[j]
            t.add(num)
    answer = list(t)
    answer.sort()
    return answer