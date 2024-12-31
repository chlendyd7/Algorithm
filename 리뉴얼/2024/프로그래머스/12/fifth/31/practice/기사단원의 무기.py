def solution(number, limit, power):
    lst = []
    answer = 0
    for i in range(1, number+1):
        temp = 0
        for j in range(1, int(i **0.5)+1):
            if i % j == 0:
                temp += 1
                if j < i // j:
                    temp += 1
        lst.append(temp)
    
    for l in lst:
        if l > limit:
            answer += power
        else:
            answer += l
    
    return answer

solution(5, 3, 2)