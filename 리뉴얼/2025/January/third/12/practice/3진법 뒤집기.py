def solution(n):
    answer = ""
    while n:
        answer += str((n % 3))
        n //= 3
    print(answer)
    return int(answer, 3)
print(solution(45))