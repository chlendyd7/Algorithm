def solution(a, b, n):
    answer = 0
    while n >= a:
        bottle = (n // a) * b
        answer += bottle
        n = n % a + bottle
        
    return answer
