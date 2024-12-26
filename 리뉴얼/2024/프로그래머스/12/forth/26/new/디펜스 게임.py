import heapq

def solution(n, k, enemy):
    if k >= len(enemy):
        return len(enemy)
    priority_q = []
    
    for idx, e in enumerate(enemy):
        heapq.heappush(priority_q, e)
        if len(priority_q) > k:
            last = heapq.heappop(priority_q)
            if last > n:
                return idx
            n -= last
    return len(enemy)
