import heapq
import sys

v, e = map(int, input().split())
start = int(input())
graph = [[] for _ in range(v+1)]
distance = [float('inf')] * (v+1)

for _ in range(e):
    u, node_v, w = map(int ,input().split())
    graph[u].append((node_v, w))

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    
    while q:
        dist, now = heapq.heappop(q)
        
        if distance[now] < dist:
            continue
        
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(start)
for i in range(1, v+1):
    if distance[i] == float('inf'):
        print('도달 할 수 없음')
    else:
        print(distance[i])
