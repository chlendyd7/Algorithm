n, m = map(int, input().split())
graph = []

def bellman_ford(start, n, graph):
    dist = [float('inf')] * (n+1)
    dist[start] = 0
    
    for i in range(n):
        for u, v, w in graph:
            if dist[u] != float('inf') and dist[v] > dist[u] + w:
                dist[v] = dist[u] + w
                if i == n-1:
                    return None
    return dist

for _ in range(m):
    graph.append(list(map(int ,input().split())))

result = bellman_ford(1,n, graph)
if result is None:
    print(-1)
else:
    for i in range(2, n+1):
        print(result[i] if result[i] != float('inf') else -1)
