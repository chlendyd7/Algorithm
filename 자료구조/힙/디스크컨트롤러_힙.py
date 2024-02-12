import heapq

def solution(jobs):
    jobs_len = len(jobs)
    jobs.sort(key=lambda x:x[0])
    heap = []
    total_time, current_time = 0, 0
    while jobs or heap:
        while jobs[0][0] <= current_time:
            job = jobs.pop(0)
            heapq.heappush(heap, (job[1], job[0]))
            print('heap:', heap)
            if heap:
                processing_time, starttime = heapq.heappop(heap)
                current_time += processing_time
                total_time += current_time - starttime
        else:
            current_time = jobs[0][0]
        
    print('totlal_time:', total_time)
    answer = total_time // jobs_len
    return answer

print(solution(jobs = [[0, 3], [1, 9], [2, 6]]))
