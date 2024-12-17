from collections import deque

def solution(people, limit):
    answer = 0
    people.sort()
    people_d = deque(people)
    
    while people_d:
        condition = people_d[0] + people_d[-1]
        if len(people_d) > 1 and condition <= limit:
            answer += 1
            people_d.pop()
            people_d.popleft()
        else:
            answer += 1
            people_d.pop()
    
    return answer

print(solution([70, 80, 50], 100))