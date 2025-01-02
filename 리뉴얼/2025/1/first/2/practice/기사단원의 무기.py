def solution(number, limit, power):
    stack = []
    for i in range(1, number + 1):
        temp = 0
        for j in range(1, int(i**0.5)+1):
            if i%j == 0:
                temp += 1
                if j < i // j:
                    temp += 1
        stack.append(temp)

    answer = 0
    for a in stack:
        if a > limit:
            answer += power
        else:
            answer += a                
    
    return answer

solution(5, 3, 2)