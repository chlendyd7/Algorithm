'''
    한 노드에서 다른 노드로 가는 거리를 입력받는 list
'''
from collections import defaultdict
import heapq
def solution(N, road, K):
    result = [1e9] + [1e9] * N
    graph = defaultdict(list)
    for s, e, v in road:
        graph[s].append((e,v))
        graph[e].append((s,v))
    
    pq = [(0, 1)]
    result[1] = 0
    
    while pq:
        now_dist, node = heapq.heappop(pq)
        if result[node] < now_dist:
            continue

        for next_node, value in graph[node]:
            if value + now_dist < result[next_node]:
                result[next_node] = value + now_dist
                heapq.heappush(pq, (value + now_dist, next_node))

    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.

    return sum(1 for r in result[1:] if r <= K)
