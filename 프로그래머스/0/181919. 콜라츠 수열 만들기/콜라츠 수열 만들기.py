def solution(n):
    result = [n]   # 시작값을 배열에 넣음
    while n != 1:
        if n % 2 == 0:      # 짝수면
            n = n // 2
        else:               # 홀수면
            n = 3 * n + 1
        result.append(n)    # 변환된 값을 배열에 추가
    return result