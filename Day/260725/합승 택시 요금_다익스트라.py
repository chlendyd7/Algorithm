import heapq

def solution(n, s, a, b, fares):
    INF = float('inf')
    
    # 인접 리스트로 그래프 구성
    graph = [[] for _ in range(n + 1)]
    for u, v, w in fares:
        graph[u].append((v, w))
        graph[v].append((u, w))
        
    def dijkstra(start):
        dist = [INF] * (n + 1)
        dist[start] = 0
        queue = [(0, start)]
        
        while queue:
            current_dist, node = heapq.heappop(queue)
            
            if current_dist > dist[node]:
                continue
                
            for neighbor, weight in graph[node]:
                cost = current_dist + weight
                if cost < dist[neighbor]:
                    dist[neighbor] = cost
                    heapq.heappush(queue, (cost, neighbor))
                    
        return dist

    # s, a, b 각각을 시작점으로 한 최단 거리 계산
    dist_s = dijkstra(s)
    dist_a = dijkstra(a)
    dist_b = dijkstra(b)
    
    # 최저 택시요금 계산
    # (s -> k) + (k -> a) + (k -> b) == dist_s[k] + dist_a[k] + dist_b[k]
    answer = INF
    for k in range(1, n + 1):
        answer = min(answer, dist_s[k] + dist_a[k] + dist_b[k])
        
    return answer