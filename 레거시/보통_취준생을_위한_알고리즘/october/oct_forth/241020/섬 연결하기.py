import heapq


def solution(n, costs):
    graph = [[] for _ in range(n+1)]

    for u, v, cost in costs:
        graph[u].append([cost,v])
        graph[v].append([cost,u])

    total_cost = 0
    visited = [False] * (n+1)
    min_heap = [(0, 1)]

    while min_heap:
        cost, u = heapq.heappop(min_heap)
        if visited[u]:
            continue
        visited[u] = True
        total_cost += cost

        for next_cost, v in graph[u]:
            if not visited[v]:
                heapq.heappush(min_heap, (next_cost, v))
    
    return total_cost

print(solution(4, [[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]))