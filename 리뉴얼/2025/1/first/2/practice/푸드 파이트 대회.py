def solution(food):
    temp = ''
    for i in range(1, len(food)):
        temp += str(i) * (food[i] // 2)
    answer = temp + '0' + temp[::-1]
    return answer
print(solution([1, 3, 4, 6]))