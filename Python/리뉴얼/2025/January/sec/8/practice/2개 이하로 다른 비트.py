def solution(numbers):
    answer = []

    for n in numbers:
        if n % 2 == 0:
            answer.append(n+1)
        else:
            bit = n + 1
            answer.append(bit + ((n ^ bit) >> 2))

    return answer