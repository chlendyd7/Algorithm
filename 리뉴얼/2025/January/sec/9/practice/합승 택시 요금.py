import heapq


def solution(n, s, a, b, fares):
    def dijkstra(start):
        distances = [float('inf')] * (n+1)
        distances[start] = 0
        pq = [(0, start)]
        while pq:
            current_distance, current_node = heapq.heappop(pq)
            if current_distance > distances[current_node]:
                continue
            for next_node, weight in graph[current_node]:
                distance = current_distance + weight
                if distance < distances[next_node]:
                    distances[next_node] = distance
                    heapq.heappush(pq, (distance, next_node))
        
        return distances

    graph = [[] for _ in range(n+1)]
    for c, d, f in fares:
        graph[c].append((d, f))
        graph[d].append((c, f))
    print(graph)    
    start_distances = dijkstra(s)
    answer = 0
    return answer