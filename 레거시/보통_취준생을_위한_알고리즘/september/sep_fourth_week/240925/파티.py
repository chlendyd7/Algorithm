import heapq
import sys


INF = sys.maxsize

def dijkstra(start, graph, N):
    distance = [INF] * (N+1)
    distance[start] = 0
    q = []
    heapq.heappush(q, (0, start))
    
    while q:
        dist, now = heapq.heappop(q)
        
        if distance[now] < dist:
            continue

        for next_node, weight in graph[now]:
            cost = dist + weight
            
            if cost < distance[next_node]:
                distance[next_node] = cost
                heapq.heappush(q, (cost, next_node))

    return distance

N, M, X = map(int,input().split())
graph =[[] for _ in range(N+1)]

for _ in range(N):
    u, v, t = map(int, input().split())
    graph[u].append((v,t))

to_X = [0] * (N+1)
for i in range(1, N+1):
    if i != X:
        to_X[i] = dijkstra(i, graph, N)[X]

from_X = dijkstra(i, graph, N)

max_time = 0
for i in range(1, N + 1):
    round_trip_time = to_X[i] + from_X[i]
    max_time = max(max_time, round_trip_time)

print(max_time)
