# https://school.programmers.co.kr/learn/courses/30/lessons/72413
from collections import defaultdict, deque
import heapq
INF = float('inf')

def solution(n, s, a, b, fares):
    def dijkstra(start):
        distance = [INF] * (n+1)
        distance[start] = 0

        q = []
        q.append((0, start))
        distance[start] = 0

        while q:
            weight, node = heapq.heappop(q)
            if distance[node] < weight:
                continue
            
            for nxt, w in graph[node]:
                nxt_weight = w + weight
                if distance[nxt] > nxt_weight:
                    distance[nxt] = nxt_weight
                    heapq.heappush(q, (nxt_weight, nxt))
        
        return distance


        
    graph = defaultdict(list)
    for a1, b1, w in fares:
        graph[a1].append((b1, w))
        graph[b1].append((a1, w))

    dist_a = dijkstra(a)
    dist_b = dijkstra(b)
    dist_s = dijkstra(s)

    answer = INF
    for k in range(1, n+1):
        answer = min(answer, dist_a[k] + dist_s[k] + dist_b[k])
    return answer