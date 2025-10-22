from collections import defaultdict
import heapq


def dijkstra(start, graph):
    distance = {node: 1e9 for node in graph}
    distance[start] = 0
    q = [(0, start)]

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


N,M,X = map(int, input().split())
graph = defaultdict(list)

for _ in range(M):
    start, end, cost = map(int, input().split())
    graph[start].append((end,cost))

to_x = {}

for i in range(1, N+1):
    if i != X:
        to_x[i] = dijkstra(i, graph)[X]

from_x = dijkstra(X, graph)

mx_time = 0
for i in range(1, N+1):
    round_trip_time = to_x.get(i,0) + from_x.get(i,0)
    mx_time = max(mx_time, round_trip_time)
