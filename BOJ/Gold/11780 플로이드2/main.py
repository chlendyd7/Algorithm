n = int(input())
m = int(input())
inf = float('inf')
graph = [[inf] *(n+1) for _ in range(n+1)]
for i in range(1, n+1):
    graph[i][i] = 0
for i in range(m):
    u,v,w = map(int, input().split())
    graph[u][v] = min(graph[u][v], w)

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            if graph[i][k] + graph[k][j] < graph[i][j]:
                graph[i][j] = graph[i][k] + graph[k][j]
    