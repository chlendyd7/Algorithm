# https://school.programmers.co.kr/learn/courses/30/lessons/42627
'''
    대기 큐,
    작업 소요시간이 짧은 것, 작업 번호가 작은 순
    그 작업만 수행
    
    시간, idx, start시간

'''

import heapq


def solution(jobs):
    answer = 0
    jobs.sort(key=lambda x: x[0])
    
    hq = []
    i = 0
    time = 0
    count = 0
    
    while count < len(jobs):
        while i < len(jobs) and jobs[i][0] <= time:
            heapq.heappush(hq, (jobs[i][1], jobs[i][0]))
            i += 1
        if hq:
            duration, start = heapq.heappop(hq)
            time += duration
            answer += (time - start)
            count += 1
        else:
            time = jobs[i][0]

    return answer // len(jobs)
        
print(solution([[0, 3], [1, 9], [3, 5]]))