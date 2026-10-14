
from collections import defaultdict
import heapq


def solution():
    V, E = map(int, input().split())
    graph = defaultdict(list)
    for _ in range(E):
        s, e, w = map(int, input().split())
        graph[s].append((w,s))
        graph[e].append((w,e))
    
    cnt = 0
    total_weight = 0
    visited = [False] * (V+1)
    hq = [(0,0)]
    while hq:
        weight, node = heapq.heappop(hq)
        
        if visited[node]:
            continue
        if cnt >= V+1:
            break
        
        for next_weight, next_node in graph[node]:
            if not visited[next_node]:
                heapq.heappush(hq, (next_weight, next_node))
                cnt += 1
                visited[next_node] = True
                total_weight += next_weight

    return total_weight


T = int(input())
for t in range(1, T+1):
    print(f'#{t} {solution()}')
