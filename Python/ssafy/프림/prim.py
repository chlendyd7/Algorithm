import heapq

def prim(n, graph, start=0):
    visited = [False] * n
    min_heap = [(0, start)]
    total_cost = 0
    mst_edges = []

    while min_heap:
        weight, u = heapq.heappop(min_heap)
        if visited[u]:
            continue

        visited[u] = True
        total_cost += weight

        if weight != 0:
            mst_edges.append((weight, u))
        
        for v, w, in graph[u]:
            if not visited[v]:
                heapq.heappush(min_heap, (w,v))
    return total_cost, mst_edges
