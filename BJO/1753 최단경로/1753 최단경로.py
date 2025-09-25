from collections import defaultdict
import heapq


V, E = map(int, input().split())
K = int(input())
#다른 모든 정점으로의 최단 경로를 구하는 프로그램..?

graph = defaultdict(list)
for _ in range(E):
    u,v,w = map(int, input().split())
    graph[u].append((v, w))

def dijkstra(start, graph):
    distance = {node: float('inf') for node in graph}
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

to_x = {}
for i in range(1, V+1):
    to_x[i] = dijkstra(i, graph)[i]

print(to_x)
