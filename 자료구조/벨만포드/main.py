INF = float('inf')

def bellman_ford(start, n, edges):
    dist = [INF] * (n+1)
    dist[start] = 0
    
    for i in range(n):
        for u, v, w in edges:
            if dist[u] != INF and dist[v] > dist[u] + w:
                dist[v] = dist[u] + w
                if i == n-1:
                    return None
    return dist

n, m = map(int, input().split())
edges = []

for _ in range(m):
    edges.append(list(map(int, input().split())))

result = bellman_ford(1,n,edges)

if result is None:
    print(-1)
else:
    for i in range(2, n+1):
        print(result[i] if result[i] != INF else "도달 불가")
