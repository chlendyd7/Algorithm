from collections import defaultdict
import heapq


def solution(n, roads, sources, destination):
    graph = defaultdict(list)
    for a, b in roads:
        graph[a].append((b, 1))
        graph[b].append((a, 1))
    
    def dijkstra(start):
        distance = [float('inf')] * (n + 1)
        distance[start] = 0
        pq = [(0, start)]

        while pq:
            current_dist, current_node = heapq.heappop(pq)

            if current_dist > distance[current_node]:
                continue

            for next_node, weight in graph[current_node]:
                dist = current_dist + weight
                if dist < distance[next_node]:
                    distance[next_node] = dist
                    heapq.heappush(pq, (distance, next_node))
        return distance
    
    min_distance = dijkstra(destination)
    answer = []
    for source in sources:
        answer