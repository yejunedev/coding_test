def solution(i, j, k):
    answer = 0

    for num in range(i, j + 1):
        for ch in str(num):
            if ch == str(k):
                answer += 1

    return answer