from collections import defaultdict
import heapq


def solution(N, road, K):
    graph = defaultdict(list)
    for a, b, c in road:
        graph[a].append((b,c))
        graph[b].append((a,c))
    
    distances = [1e9] * (N+1)
    distances[0] = 0
    distances[1] = 0

    pq = [(0,1)]

    while pq:
        curr_dist, node = heapq.heappop(pq)

        if curr_dist > distances[node]:
            continue
        
        for next_node, time in graph[node]:
            new_dist = curr_dist + time

            if new_dist < distances[next_node]:
                distances[next_node] = new_dist
                heapq.heappush(pq, (new_dist, next_node))
    
    return sum(1 for d in distances[1:] if d <= K)

