def isprime(x):
    if x==1: return False
    for i in range(2,x):
        if x%i==0:
            return False
    return True

def solution(n):
    # 약수의 개수가 세 개 이상인 수를 합성수의 갯수=
    answer = 0
    
    # 1 ~  n까지의 숫자들중 합성수 갯수
    for i in range(1,n+1):
        if i!=1 and isprime(i)==False:
            answer+=1
    
    return answer