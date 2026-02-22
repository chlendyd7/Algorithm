from collections import defaultdict
import heapq

def mst_prim(N, graph):
    visited = [0] * (N+1)
    heap = [(0, 1)]
    total = 0
    
    while heap:
        cost, node = heapq.heappop(heap)
        if visited[node]:
            continue
        visited[node] = True
        total += cost
        
        for next, cost in graph[node]:
            if not visited[next]:
                heapq.heappush(heap, (cost, next))
    return total

def solution():
    V, E = map(int, input().split())
    graph = defaultdict(list)
    for _ in range(E):
        n1, n2, cost = map(int, input().split())
        graph[n1].append((n2, cost))
        graph[n2].append((n1, cost))
    return mst_prim(V, graph)


T = int(input())
for t in range(1, T+1):
    print(f'#{t} {solution()}')