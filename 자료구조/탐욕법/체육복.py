def solution(n, lost, reserve):
    
    answer = 0
    answer = n -len(lost)
    lost.sort()
    for i in lost:
        if reserve.count(i) > 0:
            reserve.remove(i)
            answer +=1
        elif reserve.count(i-1) > 0:
            reserve.remove(i-1)
            answer +=1
        elif reserve.count(i+1) > 0:
            reserve.remove(i+1)
            answer +=1
        
    return answer

print(solution(3, [1,2,3], [1,2,3]))
print(solution(7,[1, 3, 5, 7],[1, 3, 5, 7]))
print(solution(5,[4, 5,],[3, 4,]))
