import sys
sys.stdin = open('input.txt', 'r')

from heapq import heappop, heappush

def dijkstra(start_node):
    pq = [(0, start_node)]
    dists = [INF] * V
    dists[start_node] = 0

    while pq:
        dist, node = heappop(pq)

        # 이미 더 작은 값으로 온 적이 있으면 버린다
        if dists[node] < dist:
            continue

        for next_dist, next_node in graph[node]:
            new_dist = dist + next_dist

            if dists[next_node] <= new_dist:
                continue

            # 누적거리, 새로운 노드를 pq에 저장 + dists에 갱신
            dists[next_node] = new_dist
            heappush(pq, (new_dist, next_node))
    
    return dists


INF = int(21e8) #무한대 가정

V,E = map(int, input().split())
start_node = 0
graph = [[] for _ in range(V)]

for _ in range(E):
    start, end, weight = map(int, input().split())
    graph[start].append((weight, end))

result = dijkstra(0)
