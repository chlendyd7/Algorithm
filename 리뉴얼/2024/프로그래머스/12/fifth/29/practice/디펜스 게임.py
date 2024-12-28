#수정필요
import heapq
def solution(n, k, enemy):
    q = []
    answer = 0
    if k == len(enemy):
        return k
    for e in enemy:
        if len(q) < k:
            heapq.heappush(q, e)
            continue
        else:
            if n - heapq.heappop(q) >= 0:
                answer += 1
                n -= heapq.heappop(q)
        heapq.heappush(q, e)
    return answer