import heapq


def solution(n, k, enemy):
    if k >= len(enemy):
        return len(enemy)
    q = []
    for idx, e in enumerate(enemy):
        heapq.heappush(q, e)
        if len(q) > k:
            last = heapq.heappop(q)
            if last > n:
                return idx
            n -= last
    return len(enemy)
