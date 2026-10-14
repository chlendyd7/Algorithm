'''
2. 프림 알고리즘 (Prim's Algorithm)
하나의 정점에서 시작해 인접한 간선 중 가장 낮은 비용의 간선을 선택하며 확장하는 방식입니다.
다익스트라와 구조가 매우 유사하여 사용자님께 더 익숙할 수 있습니다.
'''
import heapq
import sys

v, e = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(v + 1)]
for _ in range(e):
    u, nxt, cost = map(int, sys.stdin.readline().split())
    graph[u].append((cost, nxt))
    graph[nxt].append((cost, u))

def prim(start):
    visited = [False] * (v + 1)
    pq = [(0, start)]  # (비용, 노드)
    total_cost = 0
    count = 0  # 연결된 정점 수
    
    while pq:
        cost, curr = heapq.heappop(pq)
        
        if visited[curr]:
            continue
            
        visited[curr] = True
        total_cost += cost
        count += 1
        
        if count == v: # 모든 정점을 연결했다면 종료
            break
            
        for nxt_cost, nxt_node in graph[curr]:
            if not visited[nxt_node]:
                heapq.heappush(pq, (nxt_cost, nxt_node))
                
    return total_cost

print(prim(1))
